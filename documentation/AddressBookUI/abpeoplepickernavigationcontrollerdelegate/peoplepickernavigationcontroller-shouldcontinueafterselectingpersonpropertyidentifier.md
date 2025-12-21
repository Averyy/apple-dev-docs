# peoplePickerNavigationController(_:shouldContinueAfterSelectingPerson:property:identifier:)

**Framework**: Address Book UI  
**Kind**: method

Sent when the user selects one of a person’s properties.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func peoplePickerNavigationController(_ peoplePicker: ABPeoplePickerNavigationController, shouldContinueAfterSelectingPerson person: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to perform the action for the property selected and dismiss the picker. [`false`](https://developer.apple.com/documentation/Swift/false) to show the person in the picker.

#### Discussion

This method is called with an identifier. If you need an index, use the [`ABMultiValueGetIndexForIdentifier(_:_:)`](https://developer.apple.com/documentation/AddressBook/ABMultiValueGetIndexForIdentifier(_:_:)) function to get the corresponding index.

## Parameters

- `peoplePicker`: The people-picker navigation controller with which the user interacted.
- `person`: The person whose contact information item the user selected.
- `property`: The property the user selected.
- `identifier`: The identifier for the value the user selected if   is a multivalue property; otherwise,  .

## See Also

- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, shouldContinueAfterSelectingPerson: ABRecord) -> Bool](abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller(_:shouldcontinueafterselectingperson:).md)
  Sent when the user selects a contact.
- [func peoplePickerNavigationControllerDidCancel(ABPeoplePickerNavigationController)](abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontrollerdidcancel(_:).md)
  Sent when the user taps Cancel.
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, didSelectPerson: ABRecord)](abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller(_:didselectperson:).md)
  Called after a person has been selected by the user.
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, didSelectPerson: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier)](abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller(_:didselectperson:property:identifier:).md)
  Called after a property has been selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller(_:shouldcontinueafterselectingperson:property:identifier:))*