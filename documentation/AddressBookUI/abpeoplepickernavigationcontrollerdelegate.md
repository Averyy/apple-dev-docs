# ABPeoplePickerNavigationControllerDelegate

**Framework**: Address Book UI  
**Kind**: protocol  
**Role**: Protocol

The `ABPeoplePickerNavigationControllerDelegate` protocol describes the interface [`ABPeoplePickerNavigationController`](./abpeoplepickernavigationcontroller.md) delegates must adopt to respond to people-picker user events.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 14.0+

> **Deprecated**: Use [`CNContactPickerDelegate`](../ContactsUI/cncontactpickerdelegate.md) instead.

## Declaration

```swift
protocol ABPeoplePickerNavigationControllerDelegate : NSObjectProtocol
```

```objc
@protocol ABPeoplePickerNavigationControllerDelegate <NSObject>
```

## Topics

### Responding to User Events
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, shouldContinueAfterSelectingPerson: ABRecord) -> Bool](./abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller%28_,shouldcontinueafterselectingperson%29.md)
  Sent when the user selects a contact.
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, shouldContinueAfterSelectingPerson: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier) -> Bool](./abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller%28_,shouldcontinueafterselectingperson,property,identifier%29.md)
  Sent when the user selects one of a person’s properties.
- [func peoplePickerNavigationControllerDidCancel(ABPeoplePickerNavigationController)](./abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontrollerdidcancel%28_%29.md)
  Sent when the user taps Cancel.
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, didSelectPerson: ABRecord)](./abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller%28_,didselectperson%29.md)
  Called after a person has been selected by the user.
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, didSelectPerson: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier)](./abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller%28_,didselectperson,property,identifier%29.md)
  Called after a property has been selected by the user.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to View Controller Interactions
- [var peoplePickerDelegate: (any ABPeoplePickerNavigationControllerDelegate)?](./abpeoplepickernavigationcontroller/peoplepickerdelegate.md)
  The people-picker navigation controller delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontrollerdelegate)*