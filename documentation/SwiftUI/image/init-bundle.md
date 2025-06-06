# init(_:bundle:)

**Framework**: SwiftUI  
**Kind**: init

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

- `name`: The name of the image resource to lookup, as well as the   localization key with which to label the image.
- `bundle`: The bundle to search for the image resource and localization   content. If  , SwiftUI uses the main  . Defaults to  .

## See Also

- [init(String, variableValue: Double?, bundle: Bundle?)](image/init(_:variablevalue:bundle:).md)
  Creates a labeled image that you can use as content for controls, with a variable value.
- [init(ImageResource)](image/init(_:).md)
  Initialize an `Image` with an image resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/init(_:bundle:))*