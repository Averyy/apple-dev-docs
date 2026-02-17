# annotation

**Framework**: UIKit  
**Kind**: property

A key containing the information passed to a document interaction controller object’s annotation property.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let annotation: UIApplication.OpenURLOptionsKey
```

#### Discussion

The value of this key is a property list-typed object.

## See Also

- [static let sourceApplication: UIApplication.OpenURLOptionsKey](uiapplication/openurloptionskey/sourceapplication.md)
  A key containing the bundle ID of the app that sent the open-URL request to your app.
- [static let openInPlace: UIApplication.OpenURLOptionsKey](uiapplication/openurloptionskey/openinplace.md)
  A key containing a flag that indicates whether a document must be copied before you use it.
- [static let eventAttribution: UIApplication.OpenURLOptionsKey](uiapplication/openurloptionskey/eventattribution.md)
  An options key for `application(_:open:options:)`. The value is a `UIEventAttribution` to go along with the URL to open.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/openurloptionskey/annotation)*