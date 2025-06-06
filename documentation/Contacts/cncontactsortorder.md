# CNContactSortOrder

**Framework**: Contacts  
**Kind**: enum

Indicates the sorting order for contacts.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum CNContactSortOrder
```

#### Overview

The value [`CNContactSortOrder.userDefault`](cncontactsortorder/userdefault.md) is the user’s preferred sort order.

## Topics

### Sort Orders
- [CNContactSortOrder.none](cncontactsortorder/none.md)
  No sorting order.
- [CNContactSortOrder.userDefault](cncontactsortorder/userdefault.md)
  The user’s default sorting order.
- [CNContactSortOrder.givenName](cncontactsortorder/givenname.md)
  Sorting contacts by given name.
- [CNContactSortOrder.familyName](cncontactsortorder/familyname.md)
  Sorting contacts by family name.
### Initializers
- [init?(rawValue: Int)](cncontactsortorder/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class func descriptorForAllComparatorKeys() -> any CNKeyDescriptor](cncontact/descriptorforallcomparatorkeys.md)
  Fetches all the keys required for the contact sort comparator.
- [class func comparator(forNameSortOrder: CNContactSortOrder) -> Comparator](cncontact/comparator(fornamesortorder:).md)
  Returns a comparator to sort contacts with the specified order.
- [func isUnifiedWithContact(withIdentifier: String) -> Bool](cncontact/isunifiedwithcontact(withidentifier:).md)
  Returns a Boolean indicating whether the current contact is a unified contact and includes a contact with the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactsortorder)*