# CNContactSortOrder

**Framework**: Contacts  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum CNContactSortOrder : NSInteger;
```

#### Overview

The value [`CNContactSortOrder.userDefault`](./cncontactsortorder/userdefault.md) is the user’s preferred sort order.

## Topics

### Sort Orders
- [CNContactSortOrder.none](./cncontactsortorder/none.md)
  No sorting order.
- [CNContactSortOrder.userDefault](./cncontactsortorder/userdefault.md)
  The user’s default sorting order.
- [CNContactSortOrder.givenName](./cncontactsortorder/givenname.md)
  Sorting contacts by given name.
- [CNContactSortOrder.familyName](./cncontactsortorder/familyname.md)
  Sorting contacts by family name.
### Initializers
- [init?(rawValue: Int)](./cncontactsortorder/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Comparing Contacts
- [class func descriptorForAllComparatorKeys() -> any CNKeyDescriptor](./cncontact/descriptorforallcomparatorkeys%28%29.md)
  Fetches all the keys required for the contact sort comparator.
- [class func comparator(forNameSortOrder: CNContactSortOrder) -> Comparator](./cncontact/comparator%28fornamesortorder%29.md)
  Returns a comparator to sort contacts with the specified order.
- [func isUnifiedWithContact(withIdentifier: String) -> Bool](./cncontact/isunifiedwithcontact%28withidentifier%29.md)
  Returns a Boolean indicating whether the current contact is a unified contact and includes a contact with the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactsortorder)*