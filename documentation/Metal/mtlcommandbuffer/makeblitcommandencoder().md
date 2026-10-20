# makeBlitCommandEncoder()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a block information transfer (blit) encoder.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func makeBlitCommandEncoder() -> (any MTLBlitCommandEncoder)?
```

```objc
- (id<MTLBlitCommandEncoder>) blitCommandEncoder;
```

#### Discussion

Use an [`MTLBlitCommandEncoder`](../mtlblitcommandencoder.md) instance’s methods to create a block information transfer (blit) pass that quickly copies memory between a GPU device’s resources.

## See Also

### Creating blit encoders
- [func makeBlitCommandEncoder(descriptor: MTLBlitPassDescriptor) -> (any MTLBlitCommandEncoder)?](./makeblitcommandencoder%28descriptor%29.md)
  Creates a block information transfer (blit) encoder from a descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/makeblitcommandencoder())*