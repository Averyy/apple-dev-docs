# init(url:configuration:)

**Framework**: Safari Services  
**Kind**: init  
**Role**: Initializer

Initializes and configures a Safari view controller that loads the specified URL.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(url URL: URL, configuration: SFSafariViewController.Configuration)
```

```objc
- (instancetype) initWithURL:(NSURL *) URL configuration:(SFSafariViewControllerConfiguration *) configuration;
```

## Return Value

A newly created Safari view controller.

## Discussion

Use [`init(url:)`](./init%28url%29-5kpkn.md) to initialize an instance with the default configuration. The initializer copies the specified [`SFSafariViewController.Configuration`](./configuration-swift.class.md) object, so mutating the configuration after invoking the initializer has no effect on the view controller.

## Parameters

- `URL`: The URL to navigate to. The URL must use the `http` or `https` scheme.
- `configuration`: The configuration for the new view controller.

## See Also

### Creating a View Controller
- [SFSafariViewController.Configuration](./configuration-swift.class.md)
  A configuration object that defines how a Safari view controller should be initialized.
- [convenience init(url: URL)](./init%28url%29-5kpkn.md)
  Initializes a Safari view controller that loads the specified URL.
- [init(url: URL, entersReaderIfAvailable: Bool)](./init%28url,entersreaderifavailable%29-3aatz.md)
  Initializes a Safari view controller that will load the specified URL, entering Reader mode if Reader mode is requested and available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/init(url:configuration:)-305vl)*