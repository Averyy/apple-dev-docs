# unspecialized

**Framework**: Metal  
**Kind**: property

Defers assigning the color write mask.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static var unspecialized: MTLColorWriteMask { get }
```

#### Discussion

Until you specialize this value in the pipeline state, it behaves as `MTLColorWriteMaskAll`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcolorwritemask/unspecialized)*