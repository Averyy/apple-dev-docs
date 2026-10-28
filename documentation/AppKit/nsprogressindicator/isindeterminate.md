# isIndeterminate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the progress indicator is indeterminate.

**Availability**:
- macOS

## Declaration

```swift
var isIndeterminate: Bool { get set }
```

```objc
@property (getter=isIndeterminate) BOOL indeterminate;
```

## Discussion

A determinate indicator displays how much of the task has been completed. An indeterminate indicator shows simply that the app is busy.

When the value of this property is [`true`](../../Swift/true.md), the progress indicator is indeterminate; otherwise, it is determinate.

## See Also

### Setting the appearance
- [var controlSize: NSControl.ControlSize](./controlsize.md)
  The size of the progress indicator.
- [var style: NSProgressIndicator.Style](./style-swift.property.md)
  The style of the progress indicator (bar or spinning).
- [func sizeToFit()](./sizetofit%28%29.md)
  This action method resizes the progress indicator to an appropriate size depending on the value of [`style`](./style-swift.property.md).
- [var isDisplayedWhenStopped: Bool](./isdisplayedwhenstopped.md)
  A Boolean that indicates whether the progress indicator hides itself when it isn’t animating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/isindeterminate)*