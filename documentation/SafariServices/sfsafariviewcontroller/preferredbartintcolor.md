# preferredBarTintColor

**Framework**: Safari Services  
**Kind**: property  
**Role**: Instance Property

The color to tint the background of the navigation bar and the toolbar.

**Availability**:
- iOS 10.0+ - Deprecated in 26.0
- iPadOS 10.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0

> **Deprecated**: Tinting the bars interferes with background effects that the system provides.

## Declaration

```swift
var preferredBarTintColor: UIColor? { get set }
```

```objc
@property (nonatomic, nullable) UIColor * preferredBarTintColor;
```

#### Discussion

This color preference is ignored if the view controller is in Private Browsing mode or displaying an antiphishing warning. After the view controller is presented, changes made are not reflected.

## See Also

### Configuring the View Controller
- [var configuration: SFSafariViewController.Configuration](./configuration-swift.property.md)
  A copy of the Safari view controller’s initialized configuration.
- [var dismissButtonStyle: SFSafariViewController.DismissButtonStyle](./dismissbuttonstyle-swift.property.md)
  The style of dismiss button to use in the navigation bar to close the Safari view controller.
- [SFSafariViewController.DismissButtonStyle](./dismissbuttonstyle-swift.enum.md)
- [var preferredControlTintColor: UIColor?](./preferredcontroltintcolor.md)
  The color to tint the control buttons on the navigation bar and the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/preferredbartintcolor)*