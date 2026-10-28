# init(url:)

**Framework**: Safari Services  
**Kind**: init  
**Role**: Initializer

Initializes a Safari view controller that loads the specified URL.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
convenience init(url URL: URL)
```

```objc
- (instancetype) initWithURL:(NSURL *) URL;
```

## Return Value

A newly created Safari view controller.

## Parameters

- `URL`: The URL to navigate to. The URL must use the `http` or `https` scheme.

## See Also

### Creating a View Controller
- [init(url: URL, configuration: SFSafariViewController.Configuration)](./init%28url,configuration%29-305vl.md)
  Initializes and configures a Safari view controller that loads the specified URL.
- [SFSafariViewController.Configuration](./configuration-swift.class.md)
  A configuration object that defines how a Safari view controller should be initialized.
- [init(url: URL, entersReaderIfAvailable: Bool)](./init%28url,entersreaderifavailable%29-3aatz.md)
  Initializes a Safari view controller that will load the specified URL, entering Reader mode if Reader mode is requested and available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/init(url:)-5kpkn)*