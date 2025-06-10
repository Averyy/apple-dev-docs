# nameDoubleAction

**Framework**: Address Book  
**Kind**: property

The action to be invoked when a name is double-clicked.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
var nameDoubleAction: Selector! { get set }
```

## See Also

- [func clearSearchField(Any!)](abpeoplepickerview/clearsearchfield(_:).md)
  Clears the search field and resets the list of displayed records.
- [func editInAddressBook(Any!)](abpeoplepickerview/editinaddressbook(_:).md)
  Launches Address Book to edit the item selected in the people picker.
- [var groupDoubleAction: Selector!](abpeoplepickerview/groupdoubleaction.md)
  The action to be invoked when a group is double-clicked.
- [func selectInAddressBook(Any!)](abpeoplepickerview/selectinaddressbook(_:).md)
  Launches Address Book and selects the item selected in the people picker.
- [var target: AnyObject!](abpeoplepickerview/target.md)
  The target for double-click actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpeoplepickerview/namedoubleaction)*