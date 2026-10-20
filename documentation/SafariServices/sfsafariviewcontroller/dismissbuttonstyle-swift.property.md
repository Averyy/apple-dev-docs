# dismissButtonStyle

**Framework**: Safari Services  
**Kind**: property  
**Role**: Instance Property

The style of dismiss button to use in the navigation bar to close the Safari view controller.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var dismissButtonStyle: SFSafariViewController.DismissButtonStyle { get set }
```

```objc
@property (nonatomic) SFSafariViewControllerDismissButtonStyle dismissButtonStyle;
```

#### Discussion

The Safari view controller sets dismissButtonStyle to [`SFSafariViewController.DismissButtonStyle.close`](./dismissbuttonstyle-swift.enum/close.md) during initialization, displaying “xmark” icon by default. You can use other values such as [`SFSafariViewController.DismissButtonStyle.done`](./dismissbuttonstyle-swift.enum/done.md) to show “checkmark” icon to provide consistency with your app.

## See Also

### Configuring the View Controller
- [var configuration: SFSafariViewController.Configuration](./configuration-swift.property.md)
  A copy of the Safari view controller’s initialized configuration.
- [SFSafariViewController.DismissButtonStyle](./dismissbuttonstyle-swift.enum.md)
- [var preferredBarTintColor: UIColor?](./preferredbartintcolor.md)
  The color to tint the background of the navigation bar and the toolbar.
- [var preferredControlTintColor: UIColor?](./preferredcontroltintcolor.md)
  The color to tint the control buttons on the navigation bar and the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/dismissbuttonstyle-swift.property)*