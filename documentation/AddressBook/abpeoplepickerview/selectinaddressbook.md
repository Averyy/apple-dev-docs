# selectInAddressBook(_:)

**Framework**: Address Book  
**Kind**: method

Launches Address Book and selects the item selected in the people picker.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func selectInAddressBook(_ sender: Any!)
```

## Parameters

- `sender`: The object sending this message.

## See Also

- [func clearSearchField(Any!)](abpeoplepickerview/clearsearchfield(_:).md)
  Clears the search field and resets the list of displayed records.
- [func editInAddressBook(Any!)](abpeoplepickerview/editinaddressbook(_:).md)
  Launches Address Book to edit the item selected in the people picker.
- [var groupDoubleAction: Selector!](abpeoplepickerview/groupdoubleaction.md)
  The action to be invoked when a group is double-clicked.
- [var nameDoubleAction: Selector!](abpeoplepickerview/namedoubleaction.md)
  The action to be invoked when a name is double-clicked.
- [var target: AnyObject!](abpeoplepickerview/target.md)
  The target for double-click actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpeoplepickerview/selectinaddressbook(_:))*