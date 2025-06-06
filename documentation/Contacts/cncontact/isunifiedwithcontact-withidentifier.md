# isUnifiedWithContact(withIdentifier:)

**Framework**: Contacts  
**Kind**: method

Returns a Boolean indicating whether the current contact is a unified contact and includes a contact with the specified identifier.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func isUnifiedWithContact(withIdentifier contactIdentifier: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the current contact is a unified contact and if `contactIdentifier` represents one of the contacts that contributes to the unified information; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `contactIdentifier`: An identifier for an existing contact. If this string is empty, the method returns  .

## See Also

- [class func descriptorForAllComparatorKeys() -> any CNKeyDescriptor](cncontact/descriptorforallcomparatorkeys.md)
  Fetches all the keys required for the contact sort comparator.
- [class func comparator(forNameSortOrder: CNContactSortOrder) -> Comparator](cncontact/comparator(fornamesortorder:).md)
  Returns a comparator to sort contacts with the specified order.
- [enum CNContactSortOrder](cncontactsortorder.md)
  Indicates the sorting order for contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/isunifiedwithcontact(withidentifier:))*