# style

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The style of the progress indicator (bar or spinning).

**Availability**:
- macOS

## Declaration

```swift
var style: NSProgressIndicator.Style { get set }
```

```objc
@property NSProgressIndicatorStyle style;
```

## Discussion

See [`NSProgressIndicator.Style`](./style-swift.enum.md) for possible values.

## See Also

### Setting the appearance
- [var controlSize: NSControl.ControlSize](./controlsize.md)
  The size of the progress indicator.
- [var isIndeterminate: Bool](./isindeterminate.md)
  A Boolean that indicates whether the progress indicator is indeterminate.
- [func sizeToFit()](./sizetofit%28%29.md)
  This action method resizes the progress indicator to an appropriate size depending on the value of [`style`](./style-swift.property.md).
- [var isDisplayedWhenStopped: Bool](./isdisplayedwhenstopped.md)
  A Boolean that indicates whether the progress indicator hides itself when it isn’t animating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/style-swift.property)*