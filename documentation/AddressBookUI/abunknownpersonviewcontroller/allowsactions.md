# allowsActions

**Framework**: Address Book UI  
**Kind**: property  
**Role**: Instance Property

Specifies whether buttons appear to let the user perform actions such as sharing the contact, initiating a FaceTime call, or sending a text message.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`CNContactViewController`](../../ContactsUI/cncontactviewcontroller.md) instead.

## Declaration

```swift
var allowsActions: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsActions;
```

## Discussion

The default value is [`false`](../../Swift/false.md).

## See Also

### Configuring the Interface Details
- [var addressBook: ABAddressBook?](./addressbook.md)
  Optional. The address book database that the person record is added to.
- [var allowsAddingToAddressBook: Bool](./allowsaddingtoaddressbook.md)
  Specifies whether the user can add the properties displayed by the unknown-person view controller to the address book database, either as a new contact or by adding them to an existing contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller/allowsactions)*