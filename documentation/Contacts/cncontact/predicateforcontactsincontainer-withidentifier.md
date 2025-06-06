# predicateForContactsInContainer(withIdentifier:)

**Framework**: Contacts  
**Kind**: method

Returns a predicate to find the contacts in the specified container.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func predicateForContactsInContainer(withIdentifier containerIdentifier: String) -> NSPredicate
```

#### Return Value

A predicate that can be used to fetch contacts from [`CNContactStore`](cncontactstore.md).

## Parameters

- `containerIdentifier`: The container identifier to be matched.

## See Also

- [class func predicateForContacts(matchingName: String) -> NSPredicate](cncontact/predicateforcontacts(matchingname:).md)
  Returns a predicate to find the contacts matching the specified name.
- [class func predicateForContacts(withIdentifiers: [String]) -> NSPredicate](cncontact/predicateforcontacts(withidentifiers:).md)
  Returns a predicate to find the contacts matching the specified identifiers.
- [class func predicateForContactsInGroup(withIdentifier: String) -> NSPredicate](cncontact/predicateforcontactsingroup(withidentifier:).md)
  Returns a predicate to find the contacts that are members in the specified group.
- [class func predicateForContacts(matching: CNPhoneNumber) -> NSPredicate](cncontact/predicateforcontacts(matching:).md)
  Returns a predicate to find the contacts whose phone number matches the specified value.
- [class func predicateForContacts(matchingEmailAddress: String) -> NSPredicate](cncontact/predicateforcontacts(matchingemailaddress:).md)
  Returns a predicate to find the contacts whose email address matches the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/predicateforcontactsincontainer(withidentifier:))*