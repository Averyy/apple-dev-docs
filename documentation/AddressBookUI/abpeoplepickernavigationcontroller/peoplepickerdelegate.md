# peoplePickerDelegate

**Framework**: Address Book UI  
**Kind**: property

The people-picker navigation controller delegate.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
unowned(unsafe) var peoplePickerDelegate: (any ABPeoplePickerNavigationControllerDelegate)? { get set }
```

#### Discussion

Optional to get the selected contact, selected property or cancellation of the people picker.

## See Also

- [protocol ABPeoplePickerNavigationControllerDelegate](abpeoplepickernavigationcontrollerdelegate.md)
  The `ABPeoplePickerNavigationControllerDelegate` protocol describes the interface [`ABPeoplePickerNavigationController`](abpeoplepickernavigationcontroller.md) delegates must adopt to respond to people-picker user events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/peoplepickerdelegate)*