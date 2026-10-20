# isUnifiedWithContact(withIdentifier:)

**Framework**: Contacts  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) isUnifiedWithContactWithIdentifier:(NSString *) contactIdentifier;
```

#### Return Value

[`true`](../../Swift/true.md) if the current contact is a unified contact and if `contactIdentifier` represents one of the contacts that contributes to the unified information; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `contactIdentifier`: An identifier for an existing contact. If this string is empty, the method returns [`false`](../../Swift/false.md).

## See Also

### Comparing Contacts
- [class func descriptorForAllComparatorKeys() -> any CNKeyDescriptor](./descriptorforallcomparatorkeys%28%29.md)
  Fetches all the keys required for the contact sort comparator.
- [class func comparator(forNameSortOrder: CNContactSortOrder) -> Comparator](./comparator%28fornamesortorder%29.md)
  Returns a comparator to sort contacts with the specified order.
- [enum CNContactSortOrder](../cncontactsortorder.md)
  Indicates the sorting order for contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/isunifiedwithcontact(withidentifier:))*