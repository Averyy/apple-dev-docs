# predicateForContacts(matchingEmailAddress:)

**Framework**: Contacts  
**Kind**: method  
**Role**: Type Method

Returns a predicate to find the contacts whose email address matches the specified value.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func predicateForContacts(matchingEmailAddress emailAddress: String) -> NSPredicate
```

```objc
+ (NSPredicate *) predicateForContactsMatchingEmailAddress:(NSString *) emailAddress;
```

#### Return Value

A predicate that you can use to fetch contacts from [`CNContactStore`](../cncontactstore.md).

## Parameters

- `emailAddress`: The email address to be matched.

## See Also

### Getting Search Predicates
- [class func predicateForContacts(matchingName: String) -> NSPredicate](./predicateforcontacts%28matchingname%29.md)
  Returns a predicate to find the contacts matching the specified name.
- [class func predicateForContacts(withIdentifiers: [String]) -> NSPredicate](./predicateforcontacts%28withidentifiers%29.md)
  Returns a predicate to find the contacts matching the specified identifiers.
- [class func predicateForContactsInGroup(withIdentifier: String) -> NSPredicate](./predicateforcontactsingroup%28withidentifier%29.md)
  Returns a predicate to find the contacts that are members in the specified group.
- [class func predicateForContactsInContainer(withIdentifier: String) -> NSPredicate](./predicateforcontactsincontainer%28withidentifier%29.md)
  Returns a predicate to find the contacts in the specified container.
- [class func predicateForContacts(matching: CNPhoneNumber) -> NSPredicate](./predicateforcontacts%28matching%29.md)
  Returns a predicate to find the contacts whose phone number matches the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/predicateforcontacts(matchingemailaddress:))*