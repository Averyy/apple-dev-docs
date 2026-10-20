# isDisplayedWhenStopped

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the progress indicator hides itself when it isn’t animating.

**Availability**:
- macOS

## Declaration

```swift
var isDisplayedWhenStopped: Bool { get set }
```

```objc
@property (getter=isDisplayedWhenStopped) BOOL displayedWhenStopped;
```

#### Discussion

When the value of this property is [`false`](../../Swift/false.md), the progress indicator is hidden when it isn’t animating. The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Setting the appearance
- [var controlSize: NSControl.ControlSize](./controlsize.md)
  The size of the progress indicator.
- [var isIndeterminate: Bool](./isindeterminate.md)
  A Boolean that indicates whether the progress indicator is indeterminate.
- [var style: NSProgressIndicator.Style](./style-swift.property.md)
  The style of the progress indicator (bar or spinning).
- [func sizeToFit()](./sizetofit%28%29.md)
  This action method resizes the progress indicator to an appropriate size depending on the value of [`style`](./style-swift.property.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/isdisplayedwhenstopped)*