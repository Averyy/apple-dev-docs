# setScissorRect(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Sets a scissor rectangle to discard fragments outside a specific area.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func setScissorRect(_ rect: MTLScissorRect)
```

#### Discussion

Metal performs a scissor test and discards all fragments outside of the scissor rect.

## Parameters

- `rect`:   rectangle to specify. This rectangle needs to lie completely   within the current render attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setscissorrect(_:))*