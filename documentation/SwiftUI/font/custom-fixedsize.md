# custom(_:fixedSize:)

**Framework**: SwiftUI  
**Kind**: method

Create a custom font with the given `name` and a fixed `size` that does not scale with Dynamic Type.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static func custom(_ name: String, fixedSize: CGFloat) -> Font
```

## See Also

- [static func custom(String, size: CGFloat, relativeTo: Font.TextStyle) -> Font](font/custom(_:size:relativeto:).md)
  Create a custom font with the given `name` and `size` that scales relative to the given `textStyle`.
- [static func custom(String, size: CGFloat) -> Font](font/custom(_:size:).md)
  Create a custom font with the given `name` and `size` that scales with the body text style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/custom(_:fixedsize:))*