# UIApplication.OpenExternalURLOptionsKey

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Options for opening a URL.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
struct OpenExternalURLOptionsKey
```

```c
typedef NSString * UIApplicationOpenExternalURLOptionsKey;
```

## Topics

### URL options
- [static let universalLinksOnly: UIApplication.OpenExternalURLOptionsKey](./openexternalurloptionskey/universallinksonly.md)
  URLs must be universal links and have an app configured to open them.
### Measuring ad taps
- [static let eventAttribution: UIApplication.OpenExternalURLOptionsKey](./openexternalurloptionskey/eventattribution.md)
  An object you use to send tap event attribution data to the browser for Private Click Measurement.
### Initializers
- [init(rawValue: String)](./openexternalurloptionskey/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Opening a URL resource
- [func open(URL, options: [UIApplication.OpenExternalURLOptionsKey : Any], completionHandler: ((Bool) -> Void)?)](./open%28_,options,completionhandler%29.md)
  Attempts to asynchronously open the resource at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/openexternalurloptionskey)*