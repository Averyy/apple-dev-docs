# comparator(forNameSortOrder:)

**Framework**: Contacts  
**Kind**: method

Returns a comparator to sort contacts with the specified order.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func comparator(forNameSortOrder sortOrder: CNContactSortOrder) -> Comparator
```

#### Return Value

A comparator to order contacts.

## Parameters

- `sortOrder`: The preferred sort order, such as by given name.

## See Also

- [class func descriptorForAllComparatorKeys() -> any CNKeyDescriptor](cncontact/descriptorforallcomparatorkeys.md)
  Fetches all the keys required for the contact sort comparator.
- [func isUnifiedWithContact(withIdentifier: String) -> Bool](cncontact/isunifiedwithcontact(withidentifier:).md)
  Returns a Boolean indicating whether the current contact is a unified contact and includes a contact with the specified identifier.
- [enum CNContactSortOrder](cncontactsortorder.md)
  Indicates the sorting order for contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/comparator(fornamesortorder:))*