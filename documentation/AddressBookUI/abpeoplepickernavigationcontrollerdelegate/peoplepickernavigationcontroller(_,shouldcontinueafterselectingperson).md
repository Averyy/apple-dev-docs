# peoplePickerNavigationController(_:shouldContinueAfterSelectingPerson:)

**Framework**: Address Book UI  
**Kind**: method  
**Role**: Instance Method

Sent when the user selects a contact.

**Availability**:
- iOS 2.0+ - Deprecated in 8.0
- iPadOS 2.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`peoplePickerNavigationController(_:didSelectPerson:)`](./peoplepickernavigationcontroller%28_,didselectperson%29.md) or [`peoplePickerNavigationController(_:didSelectPerson:property:identifier:)`](./peoplepickernavigationcontroller%28_,didselectperson,property,identifier%29.md) instead.

## Declaration

```swift
optional func peoplePickerNavigationController(_ peoplePicker: ABPeoplePickerNavigationController, shouldContinueAfterSelectingPerson person: ABRecord) -> Bool
```

```objc
- (BOOL) peoplePickerNavigationController:(ABPeoplePickerNavigationController *) peoplePicker shouldContinueAfterSelectingPerson:(ABRecordRef) person;
```

#### Return Value

[`true`](../../Swift/true.md) to display the contact and dismiss the picker. [`false`](../../Swift/false.md) to do nothing.

## Parameters

- `peoplePicker`: The people-picker navigation controller with which the user interacted.
- `person`: The person the user selected.

## See Also

### Responding to User Events
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, shouldContinueAfterSelectingPerson: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier) -> Bool](./peoplepickernavigationcontroller%28_,shouldcontinueafterselectingperson,property,identifier%29.md)
  Sent when the user selects one of a person’s properties.
- [func peoplePickerNavigationControllerDidCancel(ABPeoplePickerNavigationController)](./peoplepickernavigationcontrollerdidcancel%28_%29.md)
  Sent when the user taps Cancel.
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, didSelectPerson: ABRecord)](./peoplepickernavigationcontroller%28_,didselectperson%29.md)
  Called after a person has been selected by the user.
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, didSelectPerson: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier)](./peoplepickernavigationcontroller%28_,didselectperson,property,identifier%29.md)
  Called after a property has been selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller(_:shouldcontinueafterselectingperson:))*