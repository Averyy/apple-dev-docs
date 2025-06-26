# descriptorForRequiredKeys()

**Framework**: Contacts UI  
**Kind**: method

Returns the descriptor for all the keys that must be fetched on the contact before setting it on the view controller.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class func descriptorForRequiredKeys() -> any CNKeyDescriptor
```

#### Return Value

Descriptor for all the keys that must be fetched.

#### Discussion

Pass this descriptor to the `keysToFetch` of the [`CNContactFetchRequest`](https://developer.apple.com/documentation/Contacts/CNContactFetchRequest) if you want to display the contact in a [`CNContactViewController`](cncontactviewcontroller.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/descriptorforrequiredkeys())*