# style

**Framework**: AppKit  
**Kind**: property

The style of the progress indicator (bar or spinning).

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var style: NSProgressIndicator.Style { get set }
```

#### Discussion

See [`NSProgressIndicator.Style`](nsprogressindicator/style-swift.enum.md) for possible values.

## See Also

- [var controlSize: NSControl.ControlSize](nsprogressindicator/controlsize.md)
  The size of the progress indicator.
- [var controlTint: NSControlTint](nsprogressindicator/controltint.md)
  The progress indicator’s control tint.
- [var isBezeled: Bool](nsprogressindicator/isbezeled.md)
  A Boolean that indicates whether the progress indicator’s frame has a three-dimensional bezel.
- [var isIndeterminate: Bool](nsprogressindicator/isindeterminate.md)
  A Boolean that indicates whether the progress indicator is indeterminate.
- [func sizeToFit()](nsprogressindicator/sizetofit.md)
  This action method resizes the progress indicator to an appropriate size depending on the value of [`style`](nsprogressindicator/style-swift.property.md).
- [var isDisplayedWhenStopped: Bool](nsprogressindicator/isdisplayedwhenstopped.md)
  A Boolean that indicates whether the progress indicator hides itself when it isn’t animating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/style-swift.property)*