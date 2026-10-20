# CNContactNoteKey

**Framework**: Contacts  
**Kind**: var  
**Role**: Global Variable

A note associated with a contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let CNContactNoteKey: String
```

```c
extern NSString * const CNContactNoteKey;
```

#### Discussion

This key takes a string value.

To be able to fetch the [`note`](./cncontact/note.md) property in iOS, your app needs the [`com.apple.developer.contacts.notes`](../BundleResources/entitlements/com.apple.developer.contacts.notes.md) entitlement.

## See Also

### Notes
- [com.apple.developer.contacts.notes](../BundleResources/entitlements/com.apple.developer.contacts.notes.md)
  A Boolean value that indicates whether the app may access the notes in contact entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactnotekey)*