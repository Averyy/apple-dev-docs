# custom(_:size:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Create a custom font with the given `name` and `size` that scales with the body text style.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static func custom(_ name: String, size: CGFloat) -> Font
```

## Mentions

- [Applying custom fonts to text](../applying-custom-fonts-to-text.md)

## See Also

### Creating custom fonts
- [static func custom(String, fixedSize: CGFloat) -> Font](./custom%28_,fixedsize%29.md)
  Create a custom font with the given `name` and a fixed `size` that does not scale with Dynamic Type.
- [static func custom(String, size: CGFloat, relativeTo: Font.TextStyle) -> Font](./custom%28_,size,relativeto%29.md)
  Create a custom font with the given `name` and `size` that scales relative to the given `textStyle`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/custom(_:size:))*