# allowsActions

**Framework**: Address Book UI  
**Kind**: property

Specifies whether buttons appear to let the user perform actions such as sharing the contact, initiating a FaceTime call, or sending a text message.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var allowsActions: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var addressBook: ABAddressBook?](abunknownpersonviewcontroller/addressbook.md)
  Optional. The address book database that the person record is added to.
- [var allowsAddingToAddressBook: Bool](abunknownpersonviewcontroller/allowsaddingtoaddressbook.md)
  Specifies whether the user can add the properties displayed by the unknown-person view controller to the address book database, either as a new contact or by adding them to an existing contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller/allowsactions)*