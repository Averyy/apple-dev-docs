# currentImage

**Framework**: UIKit  
**Kind**: property

The current state of the drawing context, expressed as an object that manages image data in your app.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var currentImage: UIImage { get }
```

#### Discussion

Use this property to access the current Core Graphics context as a [`UIImage`](uiimage.md) object while providing drawing instructions for one of the drawing methods in [`UIGraphicsImageRenderer`](uigraphicsimagerenderer.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsimagerenderercontext/currentimage)*