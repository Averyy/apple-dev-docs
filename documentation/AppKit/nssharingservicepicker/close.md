# close()

**Framework**: AppKit  
**Kind**: method

Closes the picker interface.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func close()
```

#### Discussion

The [`sharingServicePicker(_:didChoose:)`](nssharingservicepickerdelegate/sharingservicepicker(_:didchoose:).md) method will be invoked if the [`delegate`](nssharingservicepicker/delegate.md) is set to `nil`.

## See Also

- [func show(relativeTo: NSRect, of: NSView, preferredEdge: NSRectEdge)](nssharingservicepicker/show(relativeto:of:preferrededge:).md)
  Shows the picker interface and populates it with the relevant sharing services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicepicker/close())*