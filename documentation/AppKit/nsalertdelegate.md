# NSAlertDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A set of optional methods implemented by the delegate of an [`NSAlert`](./nsalert.md) object to respond to a user’s request for help.

**Availability**:
- macOS

## Declaration

```swift
protocol NSAlertDelegate : NSObjectProtocol
```

```objc
@protocol NSAlertDelegate <NSObject>
```

## Topics

### Displaying Help
- [func alertShowHelp(NSAlert) -> Bool](./nsalertdelegate/alertshowhelp%28_%29.md)
  Sent to the delegate when the user clicks the alert’s help button. The delegate causes help to be displayed for an alert, directly or indirectly.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Alerts
- [class NSAlert](./nsalert.md)
  A modal dialog or sheet attached to a document window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalertdelegate)*