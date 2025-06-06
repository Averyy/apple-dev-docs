# displayedKeys

**Framework**: Contacts UI  
**Kind**: property

The keys to be displayed when a contact is expanded.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var displayedKeys: [String] { get set }
```

#### Discussion

If no keys are provided, the picker selects contacts instead of values. For a list of possible keys, see [`Contact Keys`](https://developer.apple.com/documentation/Contacts/contact-keys).

## See Also

- [class CNContact](../Contacts/CNContact.md)
  An immutable object that stores information about a single contact, such as the contact’s first name, phone numbers, and addresses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactpicker/displayedkeys)*