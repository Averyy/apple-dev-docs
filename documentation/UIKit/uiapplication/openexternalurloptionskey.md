# UIApplication.OpenExternalURLOptionsKey

**Framework**: UIKit  
**Kind**: struct

Options for opening a URL.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct OpenExternalURLOptionsKey
```

## Topics

### URL options
- [static let universalLinksOnly: UIApplication.OpenExternalURLOptionsKey](uiapplication/openexternalurloptionskey/universallinksonly.md)
  URLs must be universal links and have an app configured to open them.
### Measuring ad taps
- [static let eventAttribution: UIApplication.OpenExternalURLOptionsKey](uiapplication/openexternalurloptionskey/eventattribution.md)
  An object you use to send tap event attribution data to the browser for Private Click Measurement.
### Initializers
- [init(rawValue: String)](uiapplication/openexternalurloptionskey/init(rawvalue:).md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func open(URL, options: [UIApplication.OpenExternalURLOptionsKey : Any], completionHandler: ((Bool) -> Void)?)](uiapplication/open(_:options:completionhandler:).md)
  Attempts to asynchronously open the resource at the specified URL.
- [func canOpenURL(URL) -> Bool](uiapplication/canopenurl(_:).md)
  Returns a Boolean value that indicates whether an app is available to handle a URL scheme.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/openexternalurloptionskey)*