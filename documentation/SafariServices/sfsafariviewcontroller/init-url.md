# init(url:)

**Framework**: Safari Services  
**Kind**: init

Initializes a Safari view controller that loads the specified URL.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(url URL: URL)
```

#### Return Value

A newly created Safari view controller.

## Parameters

- `URL`: The URL to navigate to. The URL must use the   or   scheme.

## See Also

- [init(url: URL, configuration: SFSafariViewController.Configuration)](sfsafariviewcontroller/init(url:configuration:).md)
  Initializes and configures a Safari view controller that loads the specified URL.
- [SFSafariViewController.Configuration](sfsafariviewcontroller/configuration-swift.class.md)
  A configuration object that defines how a Safari view controller should be initialized.
- [init(url: URL, entersReaderIfAvailable: Bool)](sfsafariviewcontroller/init(url:entersreaderifavailable:).md)
  Initializes a Safari view controller that will load the specified URL, entering Reader mode if Reader mode is requested and available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/init(url:))*