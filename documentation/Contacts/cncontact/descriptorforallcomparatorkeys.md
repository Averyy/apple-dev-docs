# descriptorForAllComparatorKeys()

**Framework**: Contacts  
**Kind**: method

Fetches all the keys required for the contact sort comparator.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func descriptorForAllComparatorKeys() -> any CNKeyDescriptor
```

#### Return Value

A descriptor object that defines the keys required by the sort comparator.

#### Discussion

Use the returned object to specify the keys you want to fetch from the database. For example, use it when creating a [`CNContactFetchRequest`](cncontactfetchrequest.md) object.

## See Also

- [class func comparator(forNameSortOrder: CNContactSortOrder) -> Comparator](cncontact/comparator(fornamesortorder:).md)
  Returns a comparator to sort contacts with the specified order.
- [func isUnifiedWithContact(withIdentifier: String) -> Bool](cncontact/isunifiedwithcontact(withidentifier:).md)
  Returns a Boolean indicating whether the current contact is a unified contact and includes a contact with the specified identifier.
- [enum CNContactSortOrder](cncontactsortorder.md)
  Indicates the sorting order for contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/descriptorforallcomparatorkeys())*