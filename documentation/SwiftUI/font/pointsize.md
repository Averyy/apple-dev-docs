# pointSize(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the point size of the font explicitly.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func pointSize(_ size: CGFloat) -> Font
```

#### Discussion

Setting the point size explicitly will result in style based fonts no longer scaling with the device’s preferred text size. To scale a font’s size relative to its current size, see [`scaled(by:)`](font/scaled(by:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/pointsize(_:))*