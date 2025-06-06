# init(url:configuration:)

**Framework**: Safari Services  
**Kind**: init

Initializes and configures a Safari view controller that loads the specified URL.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(url URL: URL, configuration: SFSafariViewController.Configuration)
```

#### Return Value

A newly created Safari view controller.

#### Discussion

Use [`init(url:)`](sfsafariviewcontroller/init(url:).md) to initialize an instance with the default configuration. The initializer copies the specified [`SFSafariViewController.Configuration`](sfsafariviewcontroller/configuration-swift.class.md) object, so mutating the configuration after invoking the initializer has no effect on the view controller.

## Parameters

- `URL`: The URL to navigate to. The URL must use the   or   scheme.
- `configuration`: The configuration for the new view controller.

## See Also

- [SFSafariViewController.Configuration](sfsafariviewcontroller/configuration-swift.class.md)
  A configuration object that defines how a Safari view controller should be initialized.
- [convenience init(url: URL)](sfsafariviewcontroller/init(url:).md)
  Initializes a Safari view controller that loads the specified URL.
- [init(url: URL, entersReaderIfAvailable: Bool)](sfsafariviewcontroller/init(url:entersreaderifavailable:).md)
  Initializes a Safari view controller that will load the specified URL, entering Reader mode if Reader mode is requested and available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/init(url:configuration:))*