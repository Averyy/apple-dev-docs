# close()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Closes the picker interface.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func close()
```

```objc
- (void) close;
```

#### Discussion

The [`sharingServicePicker(_:didChoose:)`](../nssharingservicepickerdelegate/sharingservicepicker%28_,didchoose%29.md) method will be invoked if the [`delegate`](./delegate.md) is set to `nil`.

## See Also

### Displaying the sharing service picker
- [func show(relativeTo: NSRect, of: NSView, preferredEdge: NSRectEdge)](./show%28relativeto,of,preferrededge%29.md)
  Shows the picker interface and populates it with the relevant sharing services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicepicker/close())*