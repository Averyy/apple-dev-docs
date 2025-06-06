# predicateForContacts(withIdentifiers:)

**Framework**: Contacts  
**Kind**: method

Returns a predicate to find the contacts matching the specified identifiers.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func predicateForContacts(withIdentifiers identifiers: [String]) -> NSPredicate
```

## Mentions

- [Accessing the contact store](accessing-the-contact-store.md)

#### Return Value

A predicate that can be used to fetch contacts from [`CNContactStore`](cncontactstore.md).

## Parameters

- `identifiers`: Contact identifiers to be matched.

## See Also

- [class func predicateForContacts(matchingName: String) -> NSPredicate](cncontact/predicateforcontacts(matchingname:).md)
  Returns a predicate to find the contacts matching the specified name.
- [class func predicateForContactsInGroup(withIdentifier: String) -> NSPredicate](cncontact/predicateforcontactsingroup(withidentifier:).md)
  Returns a predicate to find the contacts that are members in the specified group.
- [class func predicateForContactsInContainer(withIdentifier: String) -> NSPredicate](cncontact/predicateforcontactsincontainer(withidentifier:).md)
  Returns a predicate to find the contacts in the specified container.
- [class func predicateForContacts(matching: CNPhoneNumber) -> NSPredicate](cncontact/predicateforcontacts(matching:).md)
  Returns a predicate to find the contacts whose phone number matches the specified value.
- [class func predicateForContacts(matchingEmailAddress: String) -> NSPredicate](cncontact/predicateforcontacts(matchingemailaddress:).md)
  Returns a predicate to find the contacts whose email address matches the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/predicateforcontacts(withidentifiers:))*