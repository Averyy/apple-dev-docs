# ABUnknownPersonViewControllerDelegate

**Framework**: Address Book UI  
**Kind**: protocol  
**Role**: Protocol

The methods you use to respond to events in an unknown person view controller.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 14.0+

> **Deprecated**: Use [`CNContactViewController`](../ContactsUI/cncontactviewcontroller.md) instead.

## Declaration

```swift
protocol ABUnknownPersonViewControllerDelegate : NSObjectProtocol
```

```objc
@protocol ABUnknownPersonViewControllerDelegate <NSObject>
```

## Topics

### Responding to User Events
- [func unknownPersonViewController(ABUnknownPersonViewController, didResolveToPerson: ABRecord?)](./abunknownpersonviewcontrollerdelegate/unknownpersonviewcontroller%28_,didresolvetoperson%29.md)
  Sent when the user finishes creating a contact or adding the displayed person properties to an existing contact.
- [func unknownPersonViewController(ABUnknownPersonViewController, shouldPerformDefaultActionForPerson: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier) -> Bool](./abunknownpersonviewcontrollerdelegate/unknownpersonviewcontroller%28_,shouldperformdefaultactionforperson,property,identifier%29.md)
  Sent when the user selects a property value of the person displayed in a person view controller.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to View Controller Interactions
- [var unknownPersonViewDelegate: (any ABUnknownPersonViewControllerDelegate)?](./abunknownpersonviewcontroller/unknownpersonviewdelegate.md)
  The unknown-person view controller delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontrollerdelegate)*