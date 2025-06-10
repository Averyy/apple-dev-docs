# init(_:variableValue:bundle:)

**Framework**: SwiftUI  
**Kind**: init

Creates a labeled image that you can use as content for controls, with a variable value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(_ name: String, variableValue: Double?, bundle: Bundle? = nil)
```

#### Discussion

This initializer creates an image using a using a symbol in the specified bundle. The rendered symbol may alter its appearance to represent the value provided in `variableValue`.

> **Note**: See WWDC22 session [`10158: Adopt variable color in SF Symbols`](https://developer.apple.comhttps://developer.apple.com/wwdc22/10158/) for details on how to create symbols that support variable values.

## Parameters

- `name`: The name of the image resource to lookup, as well as   the localization key with which to label the image.
- `variableValue`: An optional value between   and   that   the rendered image can use to customize its appearance, if   specified. If the symbol doesn’t support variable values, this   parameter has no effect.
- `bundle`: The bundle to search for the image resource and   localization content. If  , SwiftUI uses the main   . Defaults to  .

## See Also

- [init(String, bundle: Bundle?)](image/init(_:bundle:).md)
  Creates a labeled image that you can use as content for controls.
- [init(ImageResource)](image/init(_:).md)
  Initialize an `Image` with an image resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/init(_:variablevalue:bundle:))*