# parentGroup

**Framework**: Address Book UI  
**Kind**: property  
**Role**: Instance Property

Optional. Specifies the group to which to add the new contact on save.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`parentGroup`](../../ContactsUI/cncontactviewcontroller/parentgroup.md) instead.

## Declaration

```swift
var parentGroup: ABRecord? { get set }
```

```objc
@property (nonatomic, readwrite, nullable) ABRecordRef parentGroup;
```

## Discussion

You must set [`addressBook`](./addressbook.md) before you can set this property.

## See Also

### Configuring New Person Views
- [var addressBook: ABAddressBook?](./addressbook.md)
  Optional. The address book to which the new contact is added.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontroller/parentgroup)*