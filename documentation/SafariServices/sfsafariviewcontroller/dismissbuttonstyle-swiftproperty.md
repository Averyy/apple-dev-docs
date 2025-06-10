# dismissButtonStyle

**Framework**: Safari Services  
**Kind**: property

The style of dismiss button to use in the navigation bar to close the Safari view controller.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var dismissButtonStyle: SFSafariViewController.DismissButtonStyle { get set }
```

#### Discussion

The Safari view controller sets dismissButtonStyle to [`SFSafariViewController.DismissButtonStyle.close`](sfsafariviewcontroller/dismissbuttonstyle-swift.enum/close.md) during initialization, displaying “xmark” icon by default. You can use other values such as [`SFSafariViewController.DismissButtonStyle.done`](sfsafariviewcontroller/dismissbuttonstyle-swift.enum/done.md) to show “checkmark” icon to provide consistency with your app.

## See Also

- [var configuration: SFSafariViewController.Configuration](sfsafariviewcontroller/configuration-swift.property.md)
  A copy of the Safari view controller’s initialized configuration.
- [SFSafariViewController.DismissButtonStyle](sfsafariviewcontroller/dismissbuttonstyle-swift.enum.md)
- [var preferredBarTintColor: UIColor?](sfsafariviewcontroller/preferredbartintcolor.md)
  The color to tint the background of the navigation bar and the toolbar.
- [var preferredControlTintColor: UIColor?](sfsafariviewcontroller/preferredcontroltintcolor.md)
  The color to tint the control buttons on the navigation bar and the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/dismissbuttonstyle-swift.property)*