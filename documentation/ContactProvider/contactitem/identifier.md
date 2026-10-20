# ContactItem.Identifier

**Framework**: ContactProvider  
**Kind**: struct  
**Role**: Structure

The app’s identifier for an item in the contact database.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
struct Identifier
```

## Topics

### Creating a contact item identifier
- [init(String)](./identifier/init%28_%29.md)
  Creates an identifier with the given value.
### Inspecting identifier properties
- [let value: String](./identifier/value.md)
  The value of the identifier.
### Accessing the root container
- [static let rootContainer: ContactItem.Identifier](./identifier/rootcontainer.md)
  The top-level container, containing the user’s contacts.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitem/identifier)*