# sourceApplication

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A key containing the bundle ID of the app that sent the open-URL request to your app.

**Availability**:
- iOS 9.0+ - Deprecated in 26.0
- iPadOS 9.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: Use UIScene lifecycle and UISceneOpenURLOptions.sourceApplication from a UIOpenURLContext in UIScene.ConnectionOptions.URLContexts instead.

## Declaration

```swift
static let sourceApplication: UIApplication.OpenURLOptionsKey
```

```c
extern UIApplicationOpenURLOptionsKey const UIApplicationOpenURLOptionsSourceApplicationKey;
```

## Discussion

The value of this key is an [`NSString`](../../../Foundation/nsstring.md) object containing the bundle ID of the app that made the request. If the request originated from another app belonging to your team, UIKit sets the value of this key to the ID of that app. If the team identifier of the originating app is different than the team identifier of the current app, the value of the key is `nil`.

## See Also

### Accessing open-URL options
- [static let annotation: UIApplication.OpenURLOptionsKey](./annotation.md)
  A key containing the information passed to a document interaction controller object’s annotation property.
- [static let openInPlace: UIApplication.OpenURLOptionsKey](./openinplace.md)
  A key containing a flag that indicates whether a document must be copied before you use it.
- [static let eventAttribution: UIApplication.OpenURLOptionsKey](./eventattribution.md)
  An options key for `application(_:open:options:)`. The value is a `UIEventAttribution` to go along with the URL to open.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/openurloptionskey/sourceapplication)*