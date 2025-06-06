# contactIdentifiers

**Framework**: CloudKit  
**Kind**: property

Identifiers that match contacts in the local Contacts database.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var contactIdentifiers: [String] { get }
```

#### Discussion

Identities that CloudKit discovers using [`CKDiscoverAllUserIdentitiesOperation`](ckdiscoveralluseridentitiesoperation.md) correspond to entries in the local Contacts database, matching the identifier on [`CNContact`](https://developer.apple.com/documentation/Contacts/CNContact).  Use these identifiers with the Contacts database to get additional information about the contacts. Multiple identifiers can exist for a single discovered user because multiple contacts can contain the same email addresses or phone numbers.

To transform these identifiers into an array of unified contact identifiers, create a predicate by calling the [`predicateForContacts(withIdentifiers:)`](https://developer.apple.com/documentation/Contacts/CNContact/predicateForContacts(withIdentifiers:)) method, and then pass that predicate to the [`unifiedContacts(matching:keysToFetch:)`](https://developer.apple.com/documentation/Contacts/CNContactStore/unifiedContacts(matching:keysToFetch:)) method.

## See Also

- [var userRecordID: CKRecord.ID?](ckuseridentity/userrecordid.md)
  The user record ID for the corresponding user record.
- [var nameComponents: PersonNameComponents?](ckuseridentity/namecomponents.md)
  The user’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckuseridentity/contactidentifiers)*