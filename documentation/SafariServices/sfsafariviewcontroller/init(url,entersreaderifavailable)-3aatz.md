# init(url:entersReaderIfAvailable:)

**Framework**: Safari Services  
**Kind**: init  
**Role**: Initializer

Initializes a Safari view controller that will load the specified URL, entering Reader mode if Reader mode is requested and available.

**Availability**:
- iOS 9.0+ - Deprecated in 11.0
- iPadOS 9.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
init(url URL: URL, entersReaderIfAvailable: Bool)
```

```objc
- (instancetype) initWithURL:(NSURL *) URL entersReaderIfAvailable:(BOOL) entersReaderIfAvailable;
```

#### Return Value

A newly created Safari view controller.

#### Discussion

`entersReaderIfAvailable` applies only to the first page loaded.

## Parameters

- `URL`: The URL to navigate to. The URL must use the `http` or `https` scheme.
- `entersReaderIfAvailable`: On output, [`true`](../../Swift/true.md) if Reader mode should be entered automatically when it is available for the webpage; otherwise, [`false`](../../Swift/false.md).

## See Also

### Creating a View Controller
- [init(url: URL, configuration: SFSafariViewController.Configuration)](./init%28url,configuration%29-305vl.md)
  Initializes and configures a Safari view controller that loads the specified URL.
- [SFSafariViewController.Configuration](./configuration-swift.class.md)
  A configuration object that defines how a Safari view controller should be initialized.
- [convenience init(url: URL)](./init%28url%29-5kpkn.md)
  Initializes a Safari view controller that loads the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/init(url:entersreaderifavailable:)-3aatz)*