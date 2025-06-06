# UIApplication.OpenURLOptionsKey

**Framework**: UIKit  
**Kind**: struct

Keys you use to access values in the options dictionary when opening a URL.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct OpenURLOptionsKey
```

#### Overview

Use these keys to retrieve options in the [`application(_:open:options:)`](uiapplicationdelegate/application(_:open:options:).md) method of your app delegate.

## Topics

### Accessing open-URL options
- [static let sourceApplication: UIApplication.OpenURLOptionsKey](uiapplication/openurloptionskey/sourceapplication.md)
  A key containing the bundle ID of the app that sent the open-URL request to your app.
- [static let annotation: UIApplication.OpenURLOptionsKey](uiapplication/openurloptionskey/annotation.md)
  A key containing the information passed to a document interaction controller object’s annotation property.
- [static let openInPlace: UIApplication.OpenURLOptionsKey](uiapplication/openurloptionskey/openinplace.md)
  A key containing a flag that indicates whether a document must be copied before you use it.
- [static let eventAttribution: UIApplication.OpenURLOptionsKey](uiapplication/openurloptionskey/eventattribution.md)
### Creating an open-URL options key
- [init(rawValue: String)](uiapplication/openurloptionskey/init(rawvalue:).md)
  Creates a URL-opening options key with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func application(UIApplication, open: URL, options: [UIApplication.OpenURLOptionsKey : Any]) -> Bool](uiapplicationdelegate/application(_:open:options:).md)
  Asks the delegate to open a resource specified by a URL, and provides a dictionary of launch options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/openurloptionskey)*