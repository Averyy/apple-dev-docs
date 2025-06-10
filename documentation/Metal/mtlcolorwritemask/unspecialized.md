# unspecialized

**Framework**: Metal  
**Kind**: property

Defers assigning the color write mask.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static var unspecialized: MTLColorWriteMask { get }
```

#### Discussion

Until you specialize this value in the pipeline state, it behaves as `MTLColorWriteMaskAll`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcolorwritemask/unspecialized)*