# ABPeoplePickerNavigationControllerDelegate

**Framework**: Address Book UI  
**Kind**: protocol

The `ABPeoplePickerNavigationControllerDelegate` protocol describes the interface [`ABPeoplePickerNavigationController`](abpeoplepickernavigationcontroller.md) delegates must adopt to respond to people-picker user events.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 14.0+

## Declaration

```swift
protocol ABPeoplePickerNavigationControllerDelegate : NSObjectProtocol
```

## Topics

### Responding to User Events
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, shouldContinueAfterSelectingPerson: ABRecord) -> Bool](abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller(_:shouldcontinueafterselectingperson:).md)
  Sent when the user selects a contact.
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, shouldContinueAfterSelectingPerson: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier) -> Bool](abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller(_:shouldcontinueafterselectingperson:property:identifier:).md)
  Sent when the user selects one of a person’s properties.
- [func peoplePickerNavigationControllerDidCancel(ABPeoplePickerNavigationController)](abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontrollerdidcancel(_:).md)
  Sent when the user taps Cancel.
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, didSelectPerson: ABRecord)](abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller(_:didselectperson:).md)
  Called after a person has been selected by the user.
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, didSelectPerson: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier)](abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller(_:didselectperson:property:identifier:).md)
  Called after a property has been selected by the user.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var peoplePickerDelegate: (any ABPeoplePickerNavigationControllerDelegate)?](abpeoplepickernavigationcontroller/peoplepickerdelegate.md)
  The people-picker navigation controller delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontrollerdelegate)*