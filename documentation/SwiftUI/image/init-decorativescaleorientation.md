# init(decorative:scale:orientation:)

**Framework**: SwiftUI  
**Kind**: init

Creates an unlabeled, decorative image based on a Core Graphics image instance.

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
init(decorative cgImage: CGImage, scale: CGFloat, orientation: Image.Orientation = .up)
```

#### Discussion

SwiftUI ignores this image for accessibility purposes.

## Parameters

- `cgImage`: The base graphical image.
- `scale`: The scale factor for the image,   with a value like  ,  , or  .
- `orientation`: The orientation of the image. The default is   .

## See Also

- [init(decorative: String, bundle: Bundle?)](image/init(decorative:bundle:).md)
  Creates an unlabeled, decorative image.
- [init(decorative: String, variableValue: Double?, bundle: Bundle?)](image/init(decorative:variablevalue:bundle:).md)
  Creates an unlabeled, decorative image, with a variable value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/init(decorative:scale:orientation:))*