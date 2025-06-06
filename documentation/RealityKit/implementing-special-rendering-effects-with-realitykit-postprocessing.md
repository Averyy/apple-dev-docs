# Implementing Special Rendering Effects with RealityKit Postprocessing

**Framework**: RealityKit

Implement a variety of postprocessing techniques to alter RealityKit rendering.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Xcode 13.3+

#### Overview

In iOS 15 and later, and macOS 12 and later, you can modify RealityKit’s rendered frame buffer before your app displays it by registering a callback function. This sample demonstrates how to create a variety of different postprocess effects for a Realitykit scene using four different technologies:

- Metal kernel functions
- Metal Performance Shaders
- Core Image
- SpriteKit rendering

It also demonstrates how to combine multiple postprocess technologies by using both Metal kernel functions and Core Image filters at the same time. The generated app displays a Reality Composer scene in AR and lets you select different postprocessing effects from a list.

##### 3971981

Because this sample app uses RealityKit, you can’t run it in Simulator — you need to run it on a device. To run this sample, you need the following:

- A Mac running macOS 12 or later
- Xcode 13 or later
- An iOS device running iOS or iPadOS 15 or later

##### 3971982

Before the app can register a callback function, it has to have one. A postprocess callback takes a single [`ARView.PostProcessContext`](arview/postprocesscontext.md) parameter and no return value. When the app registers the function, RealityKit calls it every frame before displaying the rendered scene. Any changes made to the scene are shown to the user.

The `PostProcessContext` parameter it passes to your callback function includes [`MTLTexture`](https://developer.apple.com/documentation/metal/mtltexture) containing the rendered scene, the scene’s depth map, and an output texture that the callback function uses to encode the modified framebuffer into. Once registered, the callback function must encode the modified frame buffer to `context.targetColorTexture`, or RealityKit draws nothing.

Callback functions can implement postprocessing effects using any drawing APIs as long as the app can encode the output of the API into a Metal texture. However, because RealityKit calls the function every frame, callbacks should only use APIs like Core Image and Metal kernel functions that do their work on the GPU. Modifying the frame buffer on the CPU can have a severe impact on performance and can prevent your app from rendering at a full 60 fps.

```swift
func postProcess(context: ARView.PostProcessContext) {
    // Do postprocessing here.
}
```

##### 3971983

In order to avoid hitches and other performance problems, this project performs several tasks during startup that can’t be completed in 1/60th of a second or less. For example, the glass distortion effect uses a texture, so the project loads that texture and stores it in a property before registering its callback function, like this:

```swift
guard let imageURL = Bundle.main.url(forResource: "noise",
                                     withExtension: "png") else {
    fatalError("Unable to create URL to noise texture.")
}
guard let texture = CIImage(contentsOf: imageURL) else {
    fatalError("Unable to load Musgrave.png.")
}
noiseTexture = texture
```

For each of the project’s Metal postprocessing effects, it loads the Metal kernel function and uses it to create a pipeline state property. Here’s how it loads the kernel function called `postProcessPixelate`, used to implement the pixelate effect:

```swift
guard let library = device.makeDefaultLibrary() else {
    fatalError()
}

if let pixelateKernel = library.makeFunction(name: "postProcessPixelate") {
    pixelatePipeline = try? device.makeComputePipelineState(function: pixelateKernel)
}
```

Because the project also uses Core Image effects, it creates a [`CIContext`](https://developer.apple.com/documentation/coreimage/cicontext) before registering the callback function. Unlike pipeline state properties, the project only needs one `CIContext`, even though it uses several Core Image filters.

```swift
if let device = MTLCreateSystemDefaultDevice() {
    ciContext = CIContext(mtlDevice: device)
}
```

The app also demonstrates rendering a SpriteKit scene on top of RealityKit’s frame buffer, so it loads the SpriteKit scene and creates a renderer during setup.

```swift
/// The SpriteKit scene to render.
var spriteKitScene = SKScene(fileNamed: "GameScene")

/// A renderer for doing postprocessing with SpriteKit.
var skRenderer: SKRenderer!
```

In addition to creating the SpriteKit renderer, it also configures the renderer so that it animates and renders over a clear background.

```swift
func loadSpriteKit(device: MTLDevice) {
    self.spriteKitScene?.isPaused = false
    self.skRenderer = SKRenderer(device: device)
    self.skRenderer.scene = spriteKitScene
    self.skRenderer.scene?.scaleMode = .aspectFill
    self.skRenderer.scene?.backgroundColor = .clear
    self.skRenderer.showsNodeCount = true
}
```

##### 3971984

After completing its setup tasks, the project registers its callback function with RealityKit:

```swift
arView.renderCallbacks.postProcess = self.postProcess
```

Once that code runs, RealityKit executes the callback function every frame. To disable the postprocess effect, the project could set the postprocess render callback to `nil`, like this:

```swift
arView.renderCallbacks.postProcess = self.nil
```

Rather than constantly register and unregister the callback as the user selects different options, this project takes a slightly different approach. When no postprocessing effect is active, the callback uses a [`MTLBlitCommandEncoder`](https://developer.apple.com/documentation/metal/mtlblitcommandencoder) to copy the rendered scene contained in `context.sourceColorTexture` directly to the output texture `context.targetColorTexture`, like this:

```swift
func postEffectNone(context: ARView.PostProcessContext) {
    let blitEncoder = context.commandBuffer.makeBlitCommandEncoder()
    blitEncoder?.copy(from: context.sourceColorTexture, to: context.targetColorTexture)
    blitEncoder?.endEncoding()
}
```

##### 3971985

To encode the output of its Metal kernel functions, this project uses a [`MTLComputeCommandEncoder`](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder) with the appropriate pipeline state property, like this:

```swift
guard let encoder = context.commandBuffer.makeComputeCommandEncoder() else {
    return
}

encoder.setComputePipelineState(pipeline)
parameterHandler?(encoder)

let threadsPerGrid = MTLSize(width: context.sourceColorTexture.width,
                             height: context.sourceColorTexture.height,
                             depth: 1)

let w = pixelatePipeline.threadExecutionWidth
let h = pixelatePipeline.maxTotalThreadsPerThreadgroup / w
let threadsPerThreadgroup = MTLSizeMake(w, h, 1)

encoder.dispatchThreads(threadsPerGrid,
                        threadsPerThreadgroup: threadsPerThreadgroup)
encoder.endEncoding()
```

##### 3971986

When the app is displaying a Core Image effect, it instead creates a [`CIRenderDestination`](https://developer.apple.com/documentation/coreimage/cirenderdestination) using `context.compatibleTargetTexture` as its destination. The `CIRenderDestination` encodes the result of the Core Image filter to the output texture.

```swift
func postProcessCoreImage(context: ARView.PostProcessContext,
                          filter: CIFilter) {
    
    guard let input = CIImage(mtlTexture: context.sourceColorTexture) else {
        fatalError("Unable to create CIImage from Metal texture.")
    }
    filter.setValue(input, forKey: kCIInputImageKey)
    guard let output = filter.outputImage else {
        fatalError("Error applying filter to frame buffer.")
    }
    
    let destination = CIRenderDestination(mtlTexture: context.compatibleTargetTexture,
                                          commandBuffer: context.commandBuffer)
    destination.isFlipped = false
    _ = try? self.ciContext.startTask(toRender: output, to: destination)
}
```

##### 3971987

When a Metal Performance Shader (MPS) effect is active, the project calls the filter’s [`encode(commandBuffer:sourceTexture:destinationTexture:)`](https://developer.apple.com/documentation/metalperformanceshaders/mpsunaryimagekernel/1618741-encode) method, passing the command buffer, source texture, and target texture from the context:

```swift
func postEffectLaPlacian(context: ARView.PostProcessContext) {
    let filter = MPSImageLaplacian()
    filter.encode(commandBuffer: context.commandBuffer,
                  sourceTexture: context.sourceColorTexture,
                  destinationTexture: context.compatibleTargetTexture)
}
```

##### 3971988

In addition to using kernel functions, MPS, and Core Image to process the framebuffer, this project also demonstrates how to render a SpriteKit scene on top of RealityKit’s rendered scene. In the callback function, SpriteKit renders the frame, then uses an [`MTLBlitCommandEncoder`](https://developer.apple.com/documentation/metal/mtlblitcommandencoder) to overlay the SpriteKit scene, which renders over a transparent background, on top of the frame buffer.

```swift
func postEffectSpriteKit(context: ARView.PostProcessContext) {
    let blitEncoder = context.commandBuffer.makeBlitCommandEncoder()
    blitEncoder?.copy(from: context.sourceColorTexture, to: context.targetColorTexture)
    blitEncoder?.endEncoding()
    
    let desc = MTLRenderPassDescriptor()
    desc.colorAttachments[0].loadAction = .load
    desc.colorAttachments[0].storeAction = .store
    desc.colorAttachments[0].texture = context.targetColorTexture
    
    skRenderer.update(atTime: context.time)
    skRenderer.render(withViewport: CGRect(x: 0, y: 0, width: context.targetColorTexture.width, height: context.targetColorTexture.height),
                      commandBuffer: context.commandBuffer,
                      renderPassDescriptor: desc)
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/implementing_special_rendering_effects_with_realitykit_postprocessing)*