# configuration

**Framework**: Safari Services  
**Kind**: property  
**Role**: Instance Property

A copy of the Safari view controller’s initialized configuration.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var configuration: SFSafariViewController.Configuration { get }
```

```objc
@property (nonatomic, copy, readonly) SFSafariViewControllerConfiguration * configuration;
```

## Discussion

See [`SFSafariViewController.Configuration`](./configuration-swift.class.md) for configuration properties.

## See Also

### Configuring the View Controller
- [var dismissButtonStyle: SFSafariViewController.DismissButtonStyle](./dismissbuttonstyle-swift.property.md)
  The style of dismiss button to use in the navigation bar to close the Safari view controller.
- [SFSafariViewController.DismissButtonStyle](./dismissbuttonstyle-swift.enum.md)
- [var preferredBarTintColor: UIColor?](./preferredbartintcolor.md)
  The color to tint the background of the navigation bar and the toolbar.
- [var preferredControlTintColor: UIColor?](./preferredcontroltintcolor.md)
  The color to tint the control buttons on the navigation bar and the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/configuration-swift.property)*