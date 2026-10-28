# makeBlitCommandEncoder(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a block information transfer (blit) encoder from a descriptor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func makeBlitCommandEncoder(descriptor blitPassDescriptor: MTLBlitPassDescriptor) -> (any MTLBlitCommandEncoder)?
```

```objc
- (id<MTLBlitCommandEncoder>) blitCommandEncoderWithDescriptor:(MTLBlitPassDescriptor *) blitPassDescriptor;
```

## Discussion

Use an [`MTLBlitCommandEncoder`](../mtlblitcommandencoder.md) instance’s methods to create a block information transfer (blit) pass that quickly copies memory between a GPU device’s resources.

## Parameters

- `blitPassDescriptor`: An [`MTLBlitPassDescriptor`](../mtlblitpassdescriptor.md) instance that configures the [`MTLBlitCommandEncoder`](../mtlblitcommandencoder.md) the method returns.

## See Also

### Creating blit encoders
- [func makeBlitCommandEncoder() -> (any MTLBlitCommandEncoder)?](./makeblitcommandencoder%28%29.md)
  Creates a block information transfer (blit) encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/makeblitcommandencoder(descriptor:))*