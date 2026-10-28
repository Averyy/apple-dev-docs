# addressBook

**Framework**: Address Book UI  
**Kind**: property  
**Role**: Instance Property

Optional. The address book from which to obtain the contact to display.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`CNContactViewController`](../../ContactsUI/cncontactviewcontroller.md) instead.

## Declaration

```swift
var addressBook: ABAddressBook? { get set }
```

```objc
@property (nonatomic, readwrite, nullable) ABAddressBookRef addressBook;
```

## Discussion

When unset, an address book is created and assigned to this property when needed.

## See Also

### Configuring Person Views
- [var allowsActions: Bool](./allowsactions.md)
  Specifies whether the to display buttons for actions such as sending a text message or initiating a FaceTime call.
- [var allowsEditing: Bool](./allowsediting.md)
  Specifies whether the user can edit the person’s information.
- [func setHighlightedItemForProperty(ABPropertyID, withIdentifier: ABMultiValueIdentifier)](./sethighlighteditemforproperty%28_,withidentifier%29.md)
  Specifies whether to highlight a particular property of the displayed person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/addressbook)*