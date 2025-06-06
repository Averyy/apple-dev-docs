# nameComponents

**Framework**: CloudKit  
**Kind**: property

The user’s name.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var nameComponents: PersonNameComponents? { get }
```

#### Discussion

You can use this property to construct the user’s name for display. Use the components with an instance of [`PersonNameComponentsFormatter`](https://developer.apple.com/documentation/Foundation/PersonNameComponentsFormatter) to create a string representation for the current locale.

## See Also

- [var userRecordID: CKRecord.ID?](ckuseridentity/userrecordid.md)
  The user record ID for the corresponding user record.
- [var contactIdentifiers: [String]](ckuseridentity/contactidentifiers.md)
  Identifiers that match contacts in the local Contacts database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckuseridentity/namecomponents)*