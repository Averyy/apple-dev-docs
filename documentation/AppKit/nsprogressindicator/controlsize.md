# controlSize

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The size of the progress indicator.

**Availability**:
- macOS

## Declaration

```swift
var controlSize: NSControl.ControlSize { get set }
```

```objc
@property NSControlSize controlSize;
```

#### Discussion

See [`NSCell`](../nscell.md) for possible values.

## See Also

### Setting the appearance
- [var isIndeterminate: Bool](./isindeterminate.md)
  A Boolean that indicates whether the progress indicator is indeterminate.
- [var style: NSProgressIndicator.Style](./style-swift.property.md)
  The style of the progress indicator (bar or spinning).
- [func sizeToFit()](./sizetofit%28%29.md)
  This action method resizes the progress indicator to an appropriate size depending on the value of [`style`](./style-swift.property.md).
- [var isDisplayedWhenStopped: Bool](./isdisplayedwhenstopped.md)
  A Boolean that indicates whether the progress indicator hides itself when it isn’t animating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/controlsize)*