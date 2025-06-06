# makeBlitCommandEncoder(descriptor:)

**Framework**: Metal  
**Kind**: method  
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

#### Discussion

Use an [`MTLBlitCommandEncoder`](mtlblitcommandencoder.md) instance’s methods to create a block information transfer (blit) pass that quickly copies memory between a GPU device’s resources.

## Parameters

- `blitPassDescriptor`: An   instance that configures the   the method returns.

## See Also

- [func makeBlitCommandEncoder() -> (any MTLBlitCommandEncoder)?](mtlcommandbuffer/makeblitcommandencoder.md)
  Creates a block information transfer (blit) encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/makeblitcommandencoder(descriptor:))*