# init(image:sourceRect:scale:)

**Framework**: SwiftUI  
**Kind**: init

Creates a shape-filling shape style.

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
init(image: Image, sourceRect: CGRect = CGRect(x: 0, y: 0, width: 1, height: 1), scale: CGFloat = 1)
```

## Parameters

- `image`: The image to be drawn.
- `sourceRect`: A unit-space rectangle defining how much of the source   image to draw. The results are undefined if   selects   areas outside the   range in either axis.
- `scale`: A scale factor applied to the image during rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/imagepaint/init(image:sourcerect:scale:))*