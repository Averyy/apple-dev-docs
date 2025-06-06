# peoplePickerNavigationController(_:didSelectPerson:property:identifier:)

**Framework**: Address Book UI  
**Kind**: method

Called after a property has been selected by the user.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func peoplePickerNavigationController(_ peoplePicker: ABPeoplePickerNavigationController, didSelectPerson person: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier)
```

#### Discussion

This method is called with an identifier. If you need an index, use the [`ABMultiValueGetIndexForIdentifier(_:_:)`](https://developer.apple.com/documentation/AddressBook/ABMultiValueGetIndexForIdentifier(_:_:)) function to get the corresponding index.

## Parameters

- `peoplePicker`: The people picker where the selection was made.
- `person`: The selected person record.
- `property`: The selected property.
- `identifier`: The selected property identifier.

## See Also

- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, shouldContinueAfterSelectingPerson: ABRecord) -> Bool](abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller(_:shouldcontinueafterselectingperson:).md)
  Sent when the user selects a contact.
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, shouldContinueAfterSelectingPerson: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier) -> Bool](abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller(_:shouldcontinueafterselectingperson:property:identifier:).md)
  Sent when the user selects one of a person’s properties.
- [func peoplePickerNavigationControllerDidCancel(ABPeoplePickerNavigationController)](abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontrollerdidcancel(_:).md)
  Sent when the user taps Cancel.
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, didSelectPerson: ABRecord)](abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller(_:didselectperson:).md)
  Called after a person has been selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller(_:didselectperson:property:identifier:))*