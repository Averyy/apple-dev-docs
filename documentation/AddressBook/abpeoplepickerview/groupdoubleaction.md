# groupDoubleAction

**Framework**: Address Book  
**Kind**: property  
**Role**: Instance Property

The action to be invoked when a group is double-clicked.

**Availability**:
- macOS 10.3+

## Declaration

```swift
var groupDoubleAction: Selector! { get set }
```

```objc
@property (nonatomic, assign) SEL groupDoubleAction;
```

## See Also

### Managing Actions
- [func clearSearchField(Any!)](./clearsearchfield%28_%29.md)
  Clears the search field and resets the list of displayed records.
- [func editInAddressBook(Any!)](./editinaddressbook%28_%29.md)
  Launches Address Book to edit the item selected in the people picker.
- [var nameDoubleAction: Selector!](./namedoubleaction.md)
  The action to be invoked when a name is double-clicked.
- [func selectInAddressBook(Any!)](./selectinaddressbook%28_%29.md)
  Launches Address Book and selects the item selected in the people picker.
- [var target: AnyObject!](./target.md)
  The target for double-click actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpeoplepickerview/groupdoubleaction)*