# predicateForContacts(matching:)

**Framework**: Contacts  
**Kind**: method

Returns a predicate to find the contacts whose phone number matches the specified value.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func predicateForContacts(matching phoneNumber: CNPhoneNumber) -> NSPredicate
```

#### Return Value

A predicate that you can use to fetch contacts from [`CNContactStore`](cncontactstore.md).

## Parameters

- `phoneNumber`: The phone number to be matched.

## See Also

- [class func predicateForContacts(matchingName: String) -> NSPredicate](cncontact/predicateforcontacts(matchingname:).md)
  Returns a predicate to find the contacts matching the specified name.
- [class func predicateForContacts(withIdentifiers: [String]) -> NSPredicate](cncontact/predicateforcontacts(withidentifiers:).md)
  Returns a predicate to find the contacts matching the specified identifiers.
- [class func predicateForContactsInGroup(withIdentifier: String) -> NSPredicate](cncontact/predicateforcontactsingroup(withidentifier:).md)
  Returns a predicate to find the contacts that are members in the specified group.
- [class func predicateForContactsInContainer(withIdentifier: String) -> NSPredicate](cncontact/predicateforcontactsincontainer(withidentifier:).md)
  Returns a predicate to find the contacts in the specified container.
- [class func predicateForContacts(matchingEmailAddress: String) -> NSPredicate](cncontact/predicateforcontacts(matchingemailaddress:).md)
  Returns a predicate to find the contacts whose email address matches the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/predicateforcontacts(matching:))*