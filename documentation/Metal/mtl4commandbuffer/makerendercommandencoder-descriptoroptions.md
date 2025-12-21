# makeRenderCommandEncoder(descriptor:options:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a render command encoder from a render pass descriptor with additional options.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func makeRenderCommandEncoder(descriptor: MTL4RenderPassDescriptor, options: MTL4RenderEncoderOptions = []) -> (any MTL4RenderCommandEncoder)?
```

#### Return Value

The created [`MTL4RenderCommandEncoder`](mtl4rendercommandencoder.md) instance, or `nil` if the function fails.

#### Discussion

This method creates a render command encoder to encode a render pass, whilst providing you the option to define some render pass characteristics via an instance of [`MTL4RenderEncoderOptions`](mtl4renderencoderoptions.md).

Use these options to configure suspending/resuming render command encoders, which allow you to encode render passes from multiple threads simultaneously.

## Parameters

- `descriptor`: Descriptor for the render pass.
- `options`:   instance that provide render pass options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandbuffer/makerendercommandencoder(descriptor:options:))*