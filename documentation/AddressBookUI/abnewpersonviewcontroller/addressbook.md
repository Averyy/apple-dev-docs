# addressBook

**Framework**: Address Book UI  
**Kind**: property  
**Role**: Instance Property

Optional. The address book to which the new contact is added.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`contactStore`](../../ContactsUI/cncontactviewcontroller/contactstore.md) instead.

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

### Configuring New Person Views
- [var parentGroup: ABRecord?](./parentgroup.md)
  Optional. Specifies the group to which to add the new contact on save.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontroller/addressbook)*