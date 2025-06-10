# target

**Framework**: Address Book  
**Kind**: property

The target for double-click actions.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
unowned(unsafe) var target: AnyObject! { get set }
```

#### Discussion

The target is the object on which the action specified by [`groupDoubleAction`](abpeoplepickerview/groupdoubleaction.md) and [`nameDoubleAction`](abpeoplepickerview/namedoubleaction.md) is invoked.

## See Also

- [func clearSearchField(Any!)](abpeoplepickerview/clearsearchfield(_:).md)
  Clears the search field and resets the list of displayed records.
- [func editInAddressBook(Any!)](abpeoplepickerview/editinaddressbook(_:).md)
  Launches Address Book to edit the item selected in the people picker.
- [var groupDoubleAction: Selector!](abpeoplepickerview/groupdoubleaction.md)
  The action to be invoked when a group is double-clicked.
- [var nameDoubleAction: Selector!](abpeoplepickerview/namedoubleaction.md)
  The action to be invoked when a name is double-clicked.
- [func selectInAddressBook(Any!)](abpeoplepickerview/selectinaddressbook(_:).md)
  Launches Address Book and selects the item selected in the people picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpeoplepickerview/target)*