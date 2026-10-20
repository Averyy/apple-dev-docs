# init(_:bundle:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a labeled image that you can use as content for controls.

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
init(_ name: String, bundle: Bundle? = nil)
```

## Parameters

- `name`: The name of the image resource to lookup, as well as the localization key with which to label the image.
- `bundle`: The bundle to search for the image resource and localization content. If `nil`, SwiftUI uses the main `Bundle`. Defaults to `nil`.

## See Also

### Creating an image
- [init(String, variableValue: Double?, bundle: Bundle?)](./init%28_,variablevalue,bundle%29.md)
  Creates a labeled image that you can use as content for controls, with a variable value.
- [init(ImageResource)](./init%28_%29.md)
  Initialize an `Image` with an image resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/init(_:bundle:))*