# eventAttribution

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

An options key for `application(_:open:options:)`. The value is a `UIEventAttribution` to go along with the URL to open.

**Availability**:
- iOS 14.5+ - Deprecated in 26.0
- iPadOS 14.5+ - Deprecated in 26.0
- Mac Catalyst 14.5+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: Use UIScene lifecycle and UISceneOpenURLOptions.eventAttribution from a UIOpenURLContext in UIScene.ConnectionOptions.URLContexts instead.

## Declaration

```swift
static let eventAttribution: UIApplication.OpenURLOptionsKey
```

```c
extern UIApplicationOpenURLOptionsKey const UIApplicationOpenURLOptionsEventAttributionKey;
```

## See Also

### Accessing open-URL options
- [static let sourceApplication: UIApplication.OpenURLOptionsKey](./sourceapplication.md)
  A key containing the bundle ID of the app that sent the open-URL request to your app.
- [static let annotation: UIApplication.OpenURLOptionsKey](./annotation.md)
  A key containing the information passed to a document interaction controller object’s annotation property.
- [static let openInPlace: UIApplication.OpenURLOptionsKey](./openinplace.md)
  A key containing a flag that indicates whether a document must be copied before you use it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/openurloptionskey/eventattribution)*