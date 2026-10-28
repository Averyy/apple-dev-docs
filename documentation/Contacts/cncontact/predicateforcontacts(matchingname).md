# predicateForContacts(matchingName:)

**Framework**: Contacts  
**Kind**: method  
**Role**: Type Method

Returns a predicate to find the contacts matching the specified name.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func predicateForContacts(matchingName name: String) -> NSPredicate
```

```objc
+ (NSPredicate *) predicateForContactsMatchingName:(NSString *) name;
```

## Return Value

A predicate that you can use to fetch contacts from [`CNContactStore`](../cncontactstore.md).

## Discussion

The name can contain any number of words.

## Parameters

- `name`: The contact name to be matched.

## See Also

### Getting Search Predicates
- [class func predicateForContacts(withIdentifiers: [String]) -> NSPredicate](./predicateforcontacts%28withidentifiers%29.md)
  Returns a predicate to find the contacts matching the specified identifiers.
- [class func predicateForContactsInGroup(withIdentifier: String) -> NSPredicate](./predicateforcontactsingroup%28withidentifier%29.md)
  Returns a predicate to find the contacts that are members in the specified group.
- [class func predicateForContactsInContainer(withIdentifier: String) -> NSPredicate](./predicateforcontactsincontainer%28withidentifier%29.md)
  Returns a predicate to find the contacts in the specified container.
- [class func predicateForContacts(matching: CNPhoneNumber) -> NSPredicate](./predicateforcontacts%28matching%29.md)
  Returns a predicate to find the contacts whose phone number matches the specified value.
- [class func predicateForContacts(matchingEmailAddress: String) -> NSPredicate](./predicateforcontacts%28matchingemailaddress%29.md)
  Returns a predicate to find the contacts whose email address matches the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/predicateforcontacts(matchingname:))*