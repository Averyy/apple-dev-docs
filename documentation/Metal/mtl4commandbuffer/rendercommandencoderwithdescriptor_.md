# renderCommandEncoderWithDescriptor:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Creates a render command encoder from a render pass descriptor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (id<MTL4RenderCommandEncoder>) renderCommandEncoderWithDescriptor:(MTL4RenderPassDescriptor *) descriptor;
```

## Return Value

The created [`MTL4RenderCommandEncoder`](../mtl4rendercommandencoder.md) instance, or `nil` if the function failed.

## Parameters

- `descriptor`: Descriptor for the render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandbuffer/rendercommandencoderwithdescriptor:)*