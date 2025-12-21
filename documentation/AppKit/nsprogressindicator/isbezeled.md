# isBezeled

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the progress indicator’s frame has a three-dimensional bezel.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
var isBezeled: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the progress indicator is bezeled.

## See Also

- [var controlSize: NSControl.ControlSize](nsprogressindicator/controlsize.md)
  The size of the progress indicator.
- [var controlTint: NSControlTint](nsprogressindicator/controltint.md)
  The progress indicator’s control tint.
- [var isIndeterminate: Bool](nsprogressindicator/isindeterminate.md)
  A Boolean that indicates whether the progress indicator is indeterminate.
- [var style: NSProgressIndicator.Style](nsprogressindicator/style-swift.property.md)
  The style of the progress indicator (bar or spinning).
- [func sizeToFit()](nsprogressindicator/sizetofit.md)
  This action method resizes the progress indicator to an appropriate size depending on the value of [`style`](nsprogressindicator/style-swift.property.md).
- [var isDisplayedWhenStopped: Bool](nsprogressindicator/isdisplayedwhenstopped.md)
  A Boolean that indicates whether the progress indicator hides itself when it isn’t animating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/isbezeled)*