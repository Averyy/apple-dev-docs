# ContactItem

**Framework**: ContactProvider  
**Kind**: enum

An item in the contact database.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
enum ContactItem
```

#### Overview

Your app creates instances of this type in your implementations of [`ContactItemEnumerator`](contactitemenumerator.md), delivering arrays of contact items to [`ContactItemContentObserver`](contactitemcontentobserver.md) and [`ContactItemChangeObserver`](contactitemchangeobserver.md) instances.

## Topics

### Handling item type
- [case contact(CNMutableContact, ContactItem.Identifier)](contactitem/contact(_:_:).md)
  An item that represents a person or organization.
### Identifying the item
- [ContactItem.Identifier](contactitem/identifier.md)
  The app’s identifier for an item in the contact database.
### Hashing
- [func hash(into: inout Hasher)](contactitem/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](contactitem/hashvalue.md)
  The hash value.
### Comparing contact items
- [static func == (ContactItem, ContactItem) -> Bool](contactitem/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](contactitem/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [protocol ContactItemEnumerating](contactitemenumerating.md)
  A protocol to provide enumerators for collections of contact items.
- [protocol ContactItemEnumerator](contactitemenumerator.md)
  A protocol to provide enumerations of all contact items and changed contact items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitem)*