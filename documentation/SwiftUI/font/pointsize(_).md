# pointSize(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the point size of the font explicitly.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func pointSize(_ size: CGFloat) -> Font
```

## Discussion

Setting the point size explicitly will result in style based fonts no longer scaling with the device’s preferred text size. To scale a font’s size relative to its current size, see [`scaled(by:)`](./scaled%28by%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/pointsize(_:))*