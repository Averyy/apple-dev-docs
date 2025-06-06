# sourceApplication

**Framework**: UIKit  
**Kind**: property

A key containing the bundle ID of the app that sent the open-URL request to your app.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let sourceApplication: UIApplication.OpenURLOptionsKey
```

#### Discussion

The value of this key is an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) object containing the bundle ID of the app that made the request. If the request originated from another app belonging to your team, UIKit sets the value of this key to the ID of that app. If the team identifier of the originating app is different than the team identifier of the current app, the value of the key is `nil`.

## See Also

- [static let annotation: UIApplication.OpenURLOptionsKey](uiapplication/openurloptionskey/annotation.md)
  A key containing the information passed to a document interaction controller object’s annotation property.
- [static let openInPlace: UIApplication.OpenURLOptionsKey](uiapplication/openurloptionskey/openinplace.md)
  A key containing a flag that indicates whether a document must be copied before you use it.
- [static let eventAttribution: UIApplication.OpenURLOptionsKey](uiapplication/openurloptionskey/eventattribution.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/openurloptionskey/sourceapplication)*