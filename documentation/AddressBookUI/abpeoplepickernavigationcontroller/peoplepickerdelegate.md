# peoplePickerDelegate

**Framework**: Address Book UI  
**Kind**: property  
**Role**: Instance Property

The people-picker navigation controller delegate.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`delegate`](../../ContactsUI/cncontactpickerviewcontroller/delegate.md) instead.

## Declaration

```swift
unowned(unsafe) var peoplePickerDelegate: (any ABPeoplePickerNavigationControllerDelegate)? { get set }
```

```objc
@property (nonatomic, assign, nullable) id<ABPeoplePickerNavigationControllerDelegate> peoplePickerDelegate;
```

## Discussion

Optional to get the selected contact, selected property or cancellation of the people picker.

## See Also

### Responding to View Controller Interactions
- [protocol ABPeoplePickerNavigationControllerDelegate](../abpeoplepickernavigationcontrollerdelegate.md)
  The `ABPeoplePickerNavigationControllerDelegate` protocol describes the interface [`ABPeoplePickerNavigationController`](../abpeoplepickernavigationcontroller.md) delegates must adopt to respond to people-picker user events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/peoplepickerdelegate)*