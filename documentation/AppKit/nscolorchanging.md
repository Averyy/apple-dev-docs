# NSColorChanging

**Framework**: AppKit  
**Kind**: protocol

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSColorChanging : NSObjectProtocol
```

#### Overview

When the user selects a color in an [`NSColorPanel`](nscolorpanel.md) object, the panel tries to call this method on the first responder. You can override this method in any responder that needs to respond to a color change.

## Topics

### Responding to a Color Change
- [func changeColor(NSColorPanel?)](nscolorchanging/changecolor(_:).md)
  Sent to the first responder when the user selects a color in an NSColorPanel object.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSTextView](nstextview.md)

## See Also

- [class let colorDidChangeNotification: NSNotification.Name](nscolorpanel/colordidchangenotification.md)
  Posted when the color of the `NSColorPanel` is set, as when [`NSColorPanel`](nscolorpanel.md) is invoked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorchanging)*