# init(url:entersReaderIfAvailable:)

**Framework**: Safari Services  
**Kind**: init

Initializes a Safari view controller that will load the specified URL, entering Reader mode if Reader mode is requested and available.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
init(url URL: URL, entersReaderIfAvailable: Bool)
```

#### Return Value

A newly created Safari view controller.

#### Discussion

`entersReaderIfAvailable` applies only to the first page loaded.

## Parameters

- `URL`: The URL to navigate to. The URL must use the   or   scheme.
- `entersReaderIfAvailable`: On output,   if Reader mode should be entered automatically when it is available for the webpage; otherwise,  .

## See Also

- [init(url: URL, configuration: SFSafariViewController.Configuration)](sfsafariviewcontroller/init(url:configuration:).md)
  Initializes and configures a Safari view controller that loads the specified URL.
- [SFSafariViewController.Configuration](sfsafariviewcontroller/configuration-swift.class.md)
  A configuration object that defines how a Safari view controller should be initialized.
- [convenience init(url: URL)](sfsafariviewcontroller/init(url:).md)
  Initializes a Safari view controller that loads the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/init(url:entersreaderifavailable:))*