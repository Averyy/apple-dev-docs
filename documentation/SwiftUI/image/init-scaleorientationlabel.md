# init(_:scale:orientation:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a labeled image based on a Core Graphics image instance, usable as content for controls.

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
init(_ cgImage: CGImage, scale: CGFloat, orientation: Image.Orientation = .up, label: Text)
```

## Parameters

- `cgImage`: The base graphical image.
- `scale`: The scale factor for the image,   with a value like  ,  , or  .
- `orientation`: The orientation of the image. The default is   .
- `label`: The label associated with the image. SwiftUI uses the label   for accessibility.

## See Also

- [init(String, bundle: Bundle?, label: Text)](image/init(_:bundle:label:).md)
  Creates a labeled image that you can use as content for controls, with the specified label.
- [init(String, variableValue: Double?, bundle: Bundle?, label: Text)](image/init(_:variablevalue:bundle:label:).md)
  Creates a labeled image that you can use as content for controls, with the specified label and variable value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/init(_:scale:orientation:label:))*