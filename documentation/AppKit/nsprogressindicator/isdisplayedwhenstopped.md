# isDisplayedWhenStopped

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the progress indicator hides itself when it isn’t animating.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isDisplayedWhenStopped: Bool { get set }
```

#### Discussion

When the value of this property is [`false`](https://developer.apple.com/documentation/Swift/false), the progress indicator is hidden when it isn’t animating. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var controlSize: NSControl.ControlSize](nsprogressindicator/controlsize.md)
  The size of the progress indicator.
- [var controlTint: NSControlTint](nsprogressindicator/controltint.md)
  The progress indicator’s control tint.
- [var isBezeled: Bool](nsprogressindicator/isbezeled.md)
  A Boolean that indicates whether the progress indicator’s frame has a three-dimensional bezel.
- [var isIndeterminate: Bool](nsprogressindicator/isindeterminate.md)
  A Boolean that indicates whether the progress indicator is indeterminate.
- [var style: NSProgressIndicator.Style](nsprogressindicator/style-swift.property.md)
  The style of the progress indicator (bar or spinning).
- [func sizeToFit()](nsprogressindicator/sizetofit.md)
  This action method resizes the progress indicator to an appropriate size depending on the value of [`style`](nsprogressindicator/style-swift.property.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/isdisplayedwhenstopped)*