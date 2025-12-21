# Loading entities with ShaderGraph materials

**Framework**: Reality Composer Pro

Bring entities that contain materials created with Reality Composer Pro for use in your visionOS app.

**Availability**:
- visionOS 2.0+
- Xcode 16.2+

#### Overview

Reality Composer Pro gives you the ability to create entities that you can bring over to, and interact with, in your visionOS app. This sample loads the entities created with [`ShaderGraph`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph) and places them in a [`ScrollView`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/scrollview).

![A screenshot showing three objects containing a shader graph material on them in a scroll view. The first one from the left is a blue object with vertex displacement with normal correction. The second from the left is a gradient shader. The third one from the left is a lava shader.](https://docs-assets.developer.apple.com/published/dcb1fb2cf8d614bf84bf396f95383d0b/creating-materials-overview-image%402x.jpg)

#### Create the Materials in Shadergraph

In the Project Navigator, open Packages > RealityKitContent, select `Package.realitycomposerpro`, then click Open in Reality Composer Pro.

![A screenshot.](https://docs-assets.developer.apple.com/published/2fa145792f085bc3dedb5d221d15304a/open-package-in-reality-composer-pro%402x.png)

The `RealityKitContent` package in the sample includes these shaders:

#### Create a Volumetric View in the App

The sample uses a volumetric view in a [`WindowGroup`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/windowgroup) to load the entities from the `RealityKitContent` package:

```swift
struct ShaderSamplesApp: App {
    var body: some Scene {
        WindowGroup {
            ShaderSamplesView()
        }
        .windowStyle(.volumetric)
    }
}
```

#### Load the Shaders From the Content Package

The `loadShaders` method loads all the shader entities containing the shader materials from the `ShaderSamplesScene` scene in the `realityKitContentBundle`:

```swift
private func loadShaders() async {
    guard
        let shaderSamplesSceneRoot = try? await Entity(
            named: "ShaderSamplesScene", in: realityKitContentBundle
        ).children.first
    else {
        return
    }

    // Get the shader sample entities.
    for shaderSampleEntity in shaderSamplesSceneRoot.children {
        shaderSampleEntities.append(shaderSampleEntity)
    }
}
```

The method saves the entities in a list named `shaderSampleEntities` to be used later to create the [`RealityViewContent`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/realityviewcontent).

#### Add the Shader Entities Into the Realityview Content

The `createRealityView`  method in the sample creates a [`RealityView`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/realityview) for an entity and adds it to the [`RealityViewContent`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/realityviewcontent) in the `createRealityView` method:

```swift
private func createRealityView(_ shaderSampleEntity: Entity) -> some View {
    RealityView { content in
        shaderSampleEntity.position = [0, 0, 0]
        shaderSampleEntity.scale = SIMD3<Float>(
            repeating: 0.75)
        content.add(shaderSampleEntity)
    }
    .glassBackgroundEffect()
    .containerRelativeFrame(
        [.horizontal], count: 3, spacing: 5)
}
```

The method positions the `shaderSampleEntity` at the center of the `RealityView` and reduces the scale to fit in the [`ScrollView`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/scrollview).

#### Load the Entities Into a Scrollview

The sample uses a [`ScrollView`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/scrollview) to display all the entities in the `shaderSampleEntities` list in a [`RealityView`](https://developer.apple.comhttps://developer.apple.com/documentation/RealityKit/RealityView). The `ScrollView` shows the name of the shader below the `RealityView`:

```swift
var body: some View {
    ScrollView(.horizontal) {
        HStack {
            ForEach(shaderSampleEntities) { shaderSampleEntity in
                VStack {
                    // Display the shader sample entity.
                    createRealityView(shaderSampleEntity)

                    // Display the shader name.
                    createDisplayName(shaderSampleEntity)
                }.padding([.bottom])
            }
        }
    }.task {
        // Load the shader samples scene root.
        await loadShaders()
    }
}
```

The sample loads the shaders in an asynchronous [`Task`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/task), and displays the shaders in `ScrollView`.

## See Also

- [Designing materials with Shader Graph](editor_shadergraph.md)
  Create realistic materials with Shader Graph’s node editor in Reality Composer Pro.
- [Creating a Fresnel outline effect with Shader Graph](creating-a-fresnel-outline-effect-with-shader-graph.md)
  Highlight a model by adding an outline effect.
- [Creating a vertex displacement material with Shader Graph](creating-a-vertex-displacement-material-with-shader-graph.md)
  Animate the vertices of a mesh over time with 3D Perlin noise by creating a Shader Graph material.
- [Correcting normals after vertex displacement with Shader Graph](correcting-normals-after-vertex-displacement-with-shader-graph.md)
  Approximate new vertex normals for materials that displace a mesh’s vertices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/loading-entities-with-shadergraph-materials)*