# target

**Framework**: Address Book  
**Kind**: property  
**Role**: Instance Property

The target for double-click actions.

**Availability**:
- macOS 10.3+

## Declaration

```swift
unowned(unsafe) var target: AnyObject! { get set }
```

```objc
@property (nonatomic, assign) id target;
```

#### Discussion

The target is the object on which the action specified by [`groupDoubleAction`](./groupdoubleaction.md) and [`nameDoubleAction`](./namedoubleaction.md) is invoked.

## See Also

### Managing Actions
- [func clearSearchField(Any!)](./clearsearchfield%28_%29.md)
  Clears the search field and resets the list of displayed records.
- [func editInAddressBook(Any!)](./editinaddressbook%28_%29.md)
  Launches Address Book to edit the item selected in the people picker.
- [var groupDoubleAction: Selector!](./groupdoubleaction.md)
  The action to be invoked when a group is double-clicked.
- [var nameDoubleAction: Selector!](./namedoubleaction.md)
  The action to be invoked when a name is double-clicked.
- [func selectInAddressBook(Any!)](./selectinaddressbook%28_%29.md)
  Launches Address Book and selects the item selected in the people picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpeoplepickerview/target)*