# peoplePickerNavigationController(_:shouldContinueAfterSelectingPerson:)

**Framework**: Address Book UI  
**Kind**: method

Sent when the user selects a contact.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func peoplePickerNavigationController(_ peoplePicker: ABPeoplePickerNavigationController, shouldContinueAfterSelectingPerson person: ABRecord) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to display the contact and dismiss the picker. [`false`](https://developer.apple.com/documentation/Swift/false) to do nothing.

## Parameters

- `peoplePicker`: The people-picker navigation controller with which the user interacted.
- `person`: The person the user selected.

## See Also

- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, shouldContinueAfterSelectingPerson: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier) -> Bool](abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller(_:shouldcontinueafterselectingperson:property:identifier:).md)
  Sent when the user selects one of a person’s properties.
- [func peoplePickerNavigationControllerDidCancel(ABPeoplePickerNavigationController)](abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontrollerdidcancel(_:).md)
  Sent when the user taps Cancel.
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, didSelectPerson: ABRecord)](abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller(_:didselectperson:).md)
  Called after a person has been selected by the user.
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, didSelectPerson: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier)](abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller(_:didselectperson:property:identifier:).md)
  Called after a property has been selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller(_:shouldcontinueafterselectingperson:))*