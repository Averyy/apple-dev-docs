# init(_:bundle:label:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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
- `bundle`: The bundle to search for the image resource. If `nil`, SwiftUI uses the main `Bundle`. Defaults to `nil`.
- `label`: The label associated with the image. SwiftUI uses the label for accessibility.

## See Also

### Creating an image for use as a control
- [init(String, variableValue: Double?, bundle: Bundle?, label: Text)](./init%28_,variablevalue,bundle,label%29.md)
  Creates a labeled image that you can use as content for controls, with the specified label and variable value.
- [init(CGImage, scale: CGFloat, orientation: Image.Orientation, label: Text)](./init%28_,scale,orientation,label%29.md)
  Creates a labeled image based on a Core Graphics image instance, usable as content for controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/init(_:bundle:label:))*