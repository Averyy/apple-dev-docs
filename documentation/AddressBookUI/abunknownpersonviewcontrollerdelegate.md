# ABUnknownPersonViewControllerDelegate

**Framework**: Address Book UI  
**Kind**: protocol

The methods you use to respond to events in an unknown person view controller.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 14.0+

## Declaration

```swift
protocol ABUnknownPersonViewControllerDelegate : NSObjectProtocol
```

## Topics

### Responding to User Events
- [func unknownPersonViewController(ABUnknownPersonViewController, didResolveToPerson: ABRecord?)](abunknownpersonviewcontrollerdelegate/unknownpersonviewcontroller(_:didresolvetoperson:).md)
  Sent when the user finishes creating a contact or adding the displayed person properties to an existing contact.
- [func unknownPersonViewController(ABUnknownPersonViewController, shouldPerformDefaultActionForPerson: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier) -> Bool](abunknownpersonviewcontrollerdelegate/unknownpersonviewcontroller(_:shouldperformdefaultactionforperson:property:identifier:).md)
  Sent when the user selects a property value of the person displayed in a person view controller.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var unknownPersonViewDelegate: (any ABUnknownPersonViewControllerDelegate)?](abunknownpersonviewcontroller/unknownpersonviewdelegate.md)
  The unknown-person view controller delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontrollerdelegate)*