# descriptorForRequiredKeys()

**Framework**: Contacts  
**Kind**: method

Use to fetch all contact keys required to create vCard data from a contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func descriptorForRequiredKeys() -> any CNKeyDescriptor
```

#### Return Value

A key descriptor to be used in the [`keysToFetch`](cncontactfetchrequest/keystofetch.md) array when fetching the contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactvcardserialization/descriptorforrequiredkeys())*