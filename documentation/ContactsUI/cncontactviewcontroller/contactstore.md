# contactStore

**Framework**: Contacts UI  
**Kind**: property

The contact store from which the contact was fetched or to which it will be saved.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var contactStore: CNContactStore? { get set }
```

#### Discussion

If not this property is not set, than adding the contact to the user’s contacts is disabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/contactstore)*