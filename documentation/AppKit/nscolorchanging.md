# NSColorChanging

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- macOS

## Declaration

```swift
protocol NSColorChanging : NSObjectProtocol
```

```objc
@protocol NSColorChanging <NSObject>
```

## Overview

When the user selects a color in an [`NSColorPanel`](./nscolorpanel.md) object, the panel tries to call this method on the first responder. You can override this method in any responder that needs to respond to a color change.

## Topics

### Responding to a Color Change
- [func changeColor(NSColorPanel?)](./nscolorchanging/changecolor%28_%29.md)
  Sent to the first responder when the user selects a color in an NSColorPanel object.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [NSTextView](./nstextview.md)

## See Also

### Responding to a color change
- [class let colorDidChangeNotification: NSNotification.Name](./nscolorpanel/colordidchangenotification.md)
  Posted when the color of the `NSColorPanel` is set, as when [`NSColorPanel`](./nscolorpanel.md) is invoked.
- [- changeColor:](../ObjectiveC/nsobject-swift.class/changecolor_.md)
  Sent to the first responder when the user selects a color in an `NSColorPanel` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorchanging)*