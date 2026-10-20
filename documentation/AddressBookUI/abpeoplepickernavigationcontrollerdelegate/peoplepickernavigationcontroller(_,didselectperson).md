# peoplePickerNavigationController(_:didSelectPerson:)

**Framework**: Address Book UI  
**Kind**: method  
**Role**: Instance Method

Called after a person has been selected by the user.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func peoplePickerNavigationController(_ peoplePicker: ABPeoplePickerNavigationController, didSelectPerson person: ABRecord)
```

```objc
- (void) peoplePickerNavigationController:(ABPeoplePickerNavigationController *) peoplePicker didSelectPerson:(ABRecordRef) person;
```

## Parameters

- `peoplePicker`: The people picker where the selection was made.
- `person`: The selected person record.

## See Also

### Responding to User Events
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, shouldContinueAfterSelectingPerson: ABRecord) -> Bool](./peoplepickernavigationcontroller%28_,shouldcontinueafterselectingperson%29.md)
  Sent when the user selects a contact.
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, shouldContinueAfterSelectingPerson: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier) -> Bool](./peoplepickernavigationcontroller%28_,shouldcontinueafterselectingperson,property,identifier%29.md)
  Sent when the user selects one of a person’s properties.
- [func peoplePickerNavigationControllerDidCancel(ABPeoplePickerNavigationController)](./peoplepickernavigationcontrollerdidcancel%28_%29.md)
  Sent when the user taps Cancel.
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, didSelectPerson: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier)](./peoplepickernavigationcontroller%28_,didselectperson,property,identifier%29.md)
  Called after a property has been selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontroller(_:didselectperson:))*