# controlTint

**Framework**: AppKit  
**Kind**: property

The progress indicator’s control tint.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
var controlTint: NSControlTint { get set }
```

#### Discussion

See [`NSCell`](nscell.md) for possible values.

## See Also

- [var controlSize: NSControl.ControlSize](nsprogressindicator/controlsize.md)
  The size of the progress indicator.
- [var isBezeled: Bool](nsprogressindicator/isbezeled.md)
  A Boolean that indicates whether the progress indicator’s frame has a three-dimensional bezel.
- [var isIndeterminate: Bool](nsprogressindicator/isindeterminate.md)
  A Boolean that indicates whether the progress indicator is indeterminate.
- [var style: NSProgressIndicator.Style](nsprogressindicator/style-swift.property.md)
  The style of the progress indicator (bar or spinning).
- [func sizeToFit()](nsprogressindicator/sizetofit.md)
  This action method resizes the progress indicator to an appropriate size depending on the value of [`style`](nsprogressindicator/style-swift.property.md).
- [var isDisplayedWhenStopped: Bool](nsprogressindicator/isdisplayedwhenstopped.md)
  A Boolean that indicates whether the progress indicator hides itself when it isn’t animating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/controltint)*