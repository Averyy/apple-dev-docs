# addressBook

**Framework**: Address Book UI  
**Kind**: property

Optional. The address book database that the person record is added to.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var addressBook: ABAddressBook? { get set }
```

#### Discussion

When unspecified, this view controller sets the value of this property by creating an `ABAddressBookRef` object.

The person record is only added to the address book database if [`allowsAddingToAddressBook`](abunknownpersonviewcontroller/allowsaddingtoaddressbook.md) is [`true`](https://developer.apple.com/documentation/Swift/true) and the user taps the “Add to Existing Contact” or “Create New Contact” button.

## See Also

- [var allowsActions: Bool](abunknownpersonviewcontroller/allowsactions.md)
  Specifies whether buttons appear to let the user perform actions such as sharing the contact, initiating a FaceTime call, or sending a text message.
- [var allowsAddingToAddressBook: Bool](abunknownpersonviewcontroller/allowsaddingtoaddressbook.md)
  Specifies whether the user can add the properties displayed by the unknown-person view controller to the address book database, either as a new contact or by adding them to an existing contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller/addressbook)*