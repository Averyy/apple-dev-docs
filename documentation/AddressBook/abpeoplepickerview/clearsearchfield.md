# clearSearchField(_:)

**Framework**: Address Book  
**Kind**: method

Clears the search field and resets the list of displayed records.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func clearSearchField(_ sender: Any!)
```

## Parameters

- `sender`: The object sending this message.

## See Also

- [func editInAddressBook(Any!)](abpeoplepickerview/editinaddressbook(_:).md)
  Launches Address Book to edit the item selected in the people picker.
- [var groupDoubleAction: Selector!](abpeoplepickerview/groupdoubleaction.md)
  The action to be invoked when a group is double-clicked.
- [var nameDoubleAction: Selector!](abpeoplepickerview/namedoubleaction.md)
  The action to be invoked when a name is double-clicked.
- [func selectInAddressBook(Any!)](abpeoplepickerview/selectinaddressbook(_:).md)
  Launches Address Book and selects the item selected in the people picker.
- [var target: AnyObject!](abpeoplepickerview/target.md)
  The target for double-click actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpeoplepickerview/clearsearchfield(_:))*