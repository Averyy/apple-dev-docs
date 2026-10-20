# UIApplication.OpenURLOptionsKey

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Keys you use to access values in the options dictionary when opening a URL.

**Availability**:
- iOS 9.0+ - Deprecated in 26.0
- iPadOS 9.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: Use UIScene lifecycle and equivalent properties on UISceneOpenURLOptions from a UIOpenURLContext in UIScene.ConnectionOptions.URLContexts instead.

## Declaration

```swift
struct OpenURLOptionsKey
```

```c
typedef NSString * UIApplicationOpenURLOptionsKey;
```

#### Overview

Use these keys to retrieve options in the [`application(_:open:options:)`](../uiapplicationdelegate/application%28_,open,options%29.md) method of your app delegate.

## Topics

### Accessing open-URL options
- [static let sourceApplication: UIApplication.OpenURLOptionsKey](./openurloptionskey/sourceapplication.md)
  A key containing the bundle ID of the app that sent the open-URL request to your app.
- [static let annotation: UIApplication.OpenURLOptionsKey](./openurloptionskey/annotation.md)
  A key containing the information passed to a document interaction controller object’s annotation property.
- [static let openInPlace: UIApplication.OpenURLOptionsKey](./openurloptionskey/openinplace.md)
  A key containing a flag that indicates whether a document must be copied before you use it.
- [static let eventAttribution: UIApplication.OpenURLOptionsKey](./openurloptionskey/eventattribution.md)
  An options key for `application(_:open:options:)`. The value is a `UIEventAttribution` to go along with the URL to open.
### Creating an open-URL options key
- [init(rawValue: String)](./openurloptionskey/init%28rawvalue%29.md)
  Creates a URL-opening options key with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/openurloptionskey)*