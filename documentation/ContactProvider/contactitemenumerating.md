# ContactItemEnumerating

**Framework**: ContactProvider  
**Kind**: protocol

A protocol to provide enumerators for collections of contact items.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
protocol ContactItemEnumerating
```

#### Overview

You typically implement this protocol in your app extension, since [`ContactProviderExtension`](contactproviderextension.md) inherits this protocol.

## Topics

### Providing an enumeration
- [func enumerator(for: ContactItem.Identifier) -> any ContactItemEnumerator](contactitemenumerating/enumerator(for:).md)
  Provide an enumerator for the contact items collection.
- [ContactItem.Identifier](contactitem/identifier.md)
  The app’s identifier for an item in the contact database.
- [protocol ContactItemEnumerator](contactitemenumerator.md)
  A protocol to provide enumerations of all contact items and changed contact items.

## Relationships

### Inherited By
- [ContactProviderExtension](contactproviderextension.md)

## See Also

- [enum ContactItem](contactitem.md)
  An item in the contact database.
- [protocol ContactItemEnumerator](contactitemenumerator.md)
  A protocol to provide enumerations of all contact items and changed contact items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitemenumerating)*