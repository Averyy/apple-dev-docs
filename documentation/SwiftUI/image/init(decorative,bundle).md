# init(decorative:bundle:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an unlabeled, decorative image.

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
init(decorative name: String, bundle: Bundle? = nil)
```

## Discussion

SwiftUI ignores this image for accessibility purposes.

## Parameters

- `name`: The name of the image resource to lookup
- `bundle`: The bundle to search for the image resource. If `nil`, SwiftUI uses the main `Bundle`. Defaults to `nil`.

## See Also

### Creating an image for decorative use
- [init(decorative: String, variableValue: Double?, bundle: Bundle?)](./init%28decorative,variablevalue,bundle%29.md)
  Creates an unlabeled, decorative image, with a variable value.
- [init(decorative: CGImage, scale: CGFloat, orientation: Image.Orientation)](./init%28decorative,scale,orientation%29.md)
  Creates an unlabeled, decorative image based on a Core Graphics image instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/init(decorative:bundle:))*