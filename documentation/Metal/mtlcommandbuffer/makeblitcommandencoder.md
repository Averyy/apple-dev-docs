# makeBlitCommandEncoder()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a block information transfer (blit) encoder.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func makeBlitCommandEncoder() -> (any MTLBlitCommandEncoder)?
```

#### Discussion

Use an [`MTLBlitCommandEncoder`](mtlblitcommandencoder.md) instance’s methods to create a block information transfer (blit) pass that quickly copies memory between a GPU device’s resources.

## See Also

- [func makeBlitCommandEncoder(descriptor: MTLBlitPassDescriptor) -> (any MTLBlitCommandEncoder)?](mtlcommandbuffer/makeblitcommandencoder(descriptor:).md)
  Creates a block information transfer (blit) encoder from a descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/makeblitcommandencoder())*