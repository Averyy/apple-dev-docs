# sizeToFit()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

This action method resizes the progress indicator to an appropriate size depending on the value of [`style`](./style-swift.property.md).

**Availability**:
- macOS

## Declaration

```swift
func sizeToFit()
```

```objc
- (void) sizeToFit;
```

#### Discussion

Use this after you use [`style`](./style-swift.property.md) to re-size the progress indicator.

## See Also

### Setting the appearance
- [var controlSize: NSControl.ControlSize](./controlsize.md)
  The size of the progress indicator.
- [var isIndeterminate: Bool](./isindeterminate.md)
  A Boolean that indicates whether the progress indicator is indeterminate.
- [var style: NSProgressIndicator.Style](./style-swift.property.md)
  The style of the progress indicator (bar or spinning).
- [var isDisplayedWhenStopped: Bool](./isdisplayedwhenstopped.md)
  A Boolean that indicates whether the progress indicator hides itself when it isn’t animating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/sizetofit())*