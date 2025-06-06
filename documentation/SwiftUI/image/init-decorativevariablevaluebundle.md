# init(decorative:variableValue:bundle:)

**Framework**: Swiftui  
**Kind**: init

Creates an unlabeled, decorative image, with a variable value.

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
init(decorative name: String, variableValue: Double?, bundle: Bundle? = nil)
```

#### Discussion

This initializer creates an image using a using a symbol in the specified bundle. The rendered symbol may alter its appearance to represent the value provided in `variableValue`.

> **Note**: See WWDC22 session [`10158: Adopt variable color in SF Symbols`](https://developer.apple.comhttps://developer.apple.com/wwdc22/10158/) for details on how to create symbols that support variable values.

SwiftUI ignores this image for accessibility purposes.

## Parameters

- `name`: The name of the image resource to lookup.
- `variableValue`: An optional value between   and   that   the rendered image can use to customize its appearance, if   specified. If the symbol doesn’t support variable values, this   parameter has no effect.
- `bundle`: The bundle to search for the image resource. If   , SwiftUI uses the main  . Defaults to  .

## See Also

- [init(decorative: String, bundle: Bundle?)](image/init(decorative:bundle:).md)
  Creates an unlabeled, decorative image.
- [init(decorative: CGImage, scale: CGFloat, orientation: Image.Orientation)](image/init(decorative:scale:orientation:).md)
  Creates an unlabeled, decorative image based on a Core Graphics image instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/init(decorative:variablevalue:bundle:))*