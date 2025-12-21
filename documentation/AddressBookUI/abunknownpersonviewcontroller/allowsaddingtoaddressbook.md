# allowsAddingToAddressBook

**Framework**: Address Book UI  
**Kind**: property

Specifies whether the user can add the properties displayed by the unknown-person view controller to the address book database, either as a new contact or by adding them to an existing contact.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var allowsAddingToAddressBook: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var addressBook: ABAddressBook?](abunknownpersonviewcontroller/addressbook.md)
  Optional. The address book database that the person record is added to.
- [var allowsActions: Bool](abunknownpersonviewcontroller/allowsactions.md)
  Specifies whether buttons appear to let the user perform actions such as sharing the contact, initiating a FaceTime call, or sending a text message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller/allowsaddingtoaddressbook)*