# isIndeterminate

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the progress indicator is indeterminate.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isIndeterminate: Bool { get set }
```

#### Discussion

A determinate indicator displays how much of the task has been completed. An indeterminate indicator shows simply that the app is busy.

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the progress indicator is indeterminate; otherwise, it is determinate.

## See Also

- [var controlSize: NSControl.ControlSize](nsprogressindicator/controlsize.md)
  The size of the progress indicator.
- [var controlTint: NSControlTint](nsprogressindicator/controltint.md)
  The progress indicator’s control tint.
- [var isBezeled: Bool](nsprogressindicator/isbezeled.md)
  A Boolean that indicates whether the progress indicator’s frame has a three-dimensional bezel.
- [var style: NSProgressIndicator.Style](nsprogressindicator/style-swift.property.md)
  The style of the progress indicator (bar or spinning).
- [func sizeToFit()](nsprogressindicator/sizetofit.md)
  This action method resizes the progress indicator to an appropriate size depending on the value of [`style`](nsprogressindicator/style-swift.property.md).
- [var isDisplayedWhenStopped: Bool](nsprogressindicator/isdisplayedwhenstopped.md)
  A Boolean that indicates whether the progress indicator hides itself when it isn’t animating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/isindeterminate)*