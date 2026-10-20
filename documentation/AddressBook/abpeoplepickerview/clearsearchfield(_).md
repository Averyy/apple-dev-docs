# clearSearchField(_:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Clears the search field and resets the list of displayed records.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func clearSearchField(_ sender: Any!)
```

```objc
- (void) clearSearchField:(id) sender;
```

## Parameters

- `sender`: The object sending this message.

## See Also

### Managing Actions
- [func editInAddressBook(Any!)](./editinaddressbook%28_%29.md)
  Launches Address Book to edit the item selected in the people picker.
- [var groupDoubleAction: Selector!](./groupdoubleaction.md)
  The action to be invoked when a group is double-clicked.
- [var nameDoubleAction: Selector!](./namedoubleaction.md)
  The action to be invoked when a name is double-clicked.
- [func selectInAddressBook(Any!)](./selectinaddressbook%28_%29.md)
  Launches Address Book and selects the item selected in the people picker.
- [var target: AnyObject!](./target.md)
  The target for double-click actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpeoplepickerview/clearsearchfield(_:))*