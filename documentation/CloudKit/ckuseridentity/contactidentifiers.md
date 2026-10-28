# contactIdentifiers

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

Identifiers that match contacts in the local Contacts database.

**Availability**:
- iOS 11.0+ - Deprecated in 18.0
- iPadOS 11.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.13+ - Deprecated in 15.0
- tvOS 11.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 4.0+ - Deprecated in 11.0

> **Deprecated**: No longer supported. Please see Sharing CloudKit Data with Other iCloud Users.

## Declaration

```swift
var contactIdentifiers: [String] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * contactIdentifiers;
```

## Discussion

Identities that CloudKit discovers using [`CKDiscoverAllUserIdentitiesOperation`](../ckdiscoveralluseridentitiesoperation.md) correspond to entries in the local Contacts database, matching the identifier on [`CNContact`](../../Contacts/cncontact.md).  Use these identifiers with the Contacts database to get additional information about the contacts. Multiple identifiers can exist for a single discovered user because multiple contacts can contain the same email addresses or phone numbers.

To transform these identifiers into an array of unified contact identifiers, create a predicate by calling the [`predicateForContacts(withIdentifiers:)`](../../Contacts/cncontact/predicateforcontacts%28withidentifiers%29.md) method, and then pass that predicate to the [`unifiedContacts(matching:keysToFetch:)`](../../Contacts/cncontactstore/unifiedcontacts%28matching,keystofetch%29.md) method.

## See Also

### Accessing User Information
- [var userRecordID: CKRecord.ID?](./userrecordid.md)
  The user record ID for the corresponding user record.
- [var nameComponents: PersonNameComponents?](./namecomponents.md)
  The user’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckuseridentity/contactidentifiers)*