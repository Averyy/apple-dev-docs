# init(_:bundle:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a labeled image that you can use as content for controls, with the specified label.

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
init(_ name: String, bundle: Bundle? = nil, label: Text)
```

## Parameters

- `name`: The name of the image resource to lookup
- `bundle`: The bundle to search for the image resource. If  ,   SwiftUI uses the main  . Defaults to  .
- `label`: The label associated with the image. SwiftUI uses the label   for accessibility.

## See Also

- [init(String, variableValue: Double?, bundle: Bundle?, label: Text)](image/init(_:variablevalue:bundle:label:).md)
  Creates a labeled image that you can use as content for controls, with the specified label and variable value.
- [init(CGImage, scale: CGFloat, orientation: Image.Orientation, label: Text)](image/init(_:scale:orientation:label:).md)
  Creates a labeled image based on a Core Graphics image instance, usable as content for controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/init(_:bundle:label:))*