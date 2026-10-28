# peoplePickerNavigationControllerDidCancel(_:)

**Framework**: Address Book UI  
**Kind**: method  
**Role**: Instance Method

Sent when the user taps Cancel.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func peoplePickerNavigationControllerDidCancel(_ peoplePicker: ABPeoplePickerNavigationController)
```

```objc
- (void) peoplePickerNavigationControllerDidCancel:(ABPeoplePickerNavigationController *) peoplePicker;
```

## Discussion

If the delegate does not implement this method, the people picker will dismiss itself when the user taps cancel.

### Special Considerations

Prior to iOS 8, the delegate was responsible for dismissing the people picker and this method was required.

## Parameters

- `peoplePicker`: The people-picker navigation controller with which the user interacted.

## See Also

### Responding to User Events
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, shouldContinueAfterSelectingPerson: ABRecord) -> Bool](./peoplepickernavigationcontroller%28_,shouldcontinueafterselectingperson%29.md)
  Sent when the user selects a contact.
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, shouldContinueAfterSelectingPerson: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier) -> Bool](./peoplepickernavigationcontroller%28_,shouldcontinueafterselectingperson,property,identifier%29.md)
  Sent when the user selects one of a person’s properties.
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, didSelectPerson: ABRecord)](./peoplepickernavigationcontroller%28_,didselectperson%29.md)
  Called after a person has been selected by the user.
- [func peoplePickerNavigationController(ABPeoplePickerNavigationController, didSelectPerson: ABRecord, property: ABPropertyID, identifier: ABMultiValueIdentifier)](./peoplepickernavigationcontroller%28_,didselectperson,property,identifier%29.md)
  Called after a property has been selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontrollerdelegate/peoplepickernavigationcontrollerdidcancel(_:))*