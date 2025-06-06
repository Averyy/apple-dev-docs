# preferredBarTintColor

**Framework**: Safari Services  
**Kind**: property

The color to tint the background of the navigation bar and the toolbar.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var preferredBarTintColor: UIColor? { get set }
```

#### Discussion

This color preference is ignored if the view controller is in Private Browsing mode or displaying an antiphishing warning. After the view controller is presented, changes made are not reflected.

## See Also

- [var configuration: SFSafariViewController.Configuration](sfsafariviewcontroller/configuration-swift.property.md)
  A copy of the Safari view controller’s initialized configuration.
- [var dismissButtonStyle: SFSafariViewController.DismissButtonStyle](sfsafariviewcontroller/dismissbuttonstyle-swift.property.md)
- [SFSafariViewController.DismissButtonStyle](sfsafariviewcontroller/dismissbuttonstyle-swift.enum.md)
- [var preferredControlTintColor: UIColor?](sfsafariviewcontroller/preferredcontroltintcolor.md)
  The color to tint the control buttons on the navigation bar and the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/preferredbartintcolor)*