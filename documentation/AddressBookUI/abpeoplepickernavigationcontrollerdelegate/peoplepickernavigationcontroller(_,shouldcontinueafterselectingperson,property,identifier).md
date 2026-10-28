# peoplePickerNavigationController(_:shouldContinueAfterSelectingPerson:property:identifier:)

**Framework**: Address Book UI  
**Kind**: method  
**Role**: Instance Method

Sent when the user selects one of a person’s properties.

**Availability**:
- iOS 2.0+ - Deprecated in 8.0
- iPadOS 2.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`peoplePickerNavigationController(_:didSelectPerson:)`](./peoplepickernavigationcontroller%28_,didselectperson%29.md) or [`peoplePickerNavigationController(_:didSelectPerson:property:identifier:)`](./peoplepickernavigationcontroller%28_,didselectperson,property,identifier%29.md) instead.

## Declaration

```swift
optional func peoplePickerNavigationController(_ peoplePicker: ABPeoplePickerNavigationController, shouldContinueAfterSelectingPerson person: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier) -> Bool
```

```objc
- (BOOL) peoplePickerNavigationController:(ABPeoplePickerNavigationController *) peoplePicker shouldContinueAfterSelectingPerson:(ABRecordRef) person property:(ABPropertyID) property identifier:(ABMultiValueIdentifier) identifier;
```

## Return Value

[`true`](../../Swift/true.md) to perform the action for the property selected and dismiss the picker. [`false`](../../Swift/false.md) to show the person in the picker.

## Discussion

This method is called with an identifier. If you need an index, use the [`ABMultiValueGetIndexForIdentifier(_:_:)`](../../AddressBook/abmultivaluegetindexforidentifier%28_,_%29.md) function to get the corresponding index.

## Parameters

- `peoplePicker`: The people-picker navigation controller with which the user interacted.
- `person`: The person whose contact information item the user selected.
- `property`: The property the user selected.
- `identifier`: The identifier for the value the user selected if `property` is a multivalue property; otherwise, `kABMultiValueInvalidIdentifier`.

## See Also

### Responding to User Events
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, shouldContinueAfterSelectingPerson: ABRecord) -> Bool](./peoplepickernavigationcontroller%28_,shouldcontinueafterselectingperson%29.md)
  Sent when the user selects a contact.
- [func peoplePickerNavigationControllerDidCancel(ABPeoplePickerNavigationController)](./peoplepickernavigationcontrollerdidcancel%28_%29.md)
  Sent when the user taps Cancel.
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, didSelectPerson: ABRecord)](./peoplepickernavigationcontroller%28_,didselectperson%29.md)
  Called after a person has been selected by the user.
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, didSelectPerson: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier)](./peoplepickernavigationcontroller%28_,didselectperson,property,identifier%29.md)
  Called after a property has been selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller(_:shouldcontinueafterselectingperson:property:identifier:))*