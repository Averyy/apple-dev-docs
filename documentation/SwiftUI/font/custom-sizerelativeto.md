# custom(_:size:relativeTo:)

**Framework**: SwiftUI  
**Kind**: method

Create a custom font with the given `name` and `size` that scales relative to the given `textStyle`.

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
static func custom(_ name: String, size: CGFloat, relativeTo textStyle: Font.TextStyle) -> Font
```

## See Also

- [static func custom(String, fixedSize: CGFloat) -> Font](font/custom(_:fixedsize:).md)
  Create a custom font with the given `name` and a fixed `size` that does not scale with Dynamic Type.
- [static func custom(String, size: CGFloat) -> Font](font/custom(_:size:).md)
  Create a custom font with the given `name` and `size` that scales with the body text style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/custom(_:size:relativeto:))*