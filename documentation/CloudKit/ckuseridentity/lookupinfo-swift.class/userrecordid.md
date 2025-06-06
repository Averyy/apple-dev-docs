# userRecordID

**Framework**: CloudKit  
**Kind**: property

The ID of the user record.

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
@NSCopying
var userRecordID: CKRecord.ID? { get }
```

#### Discussion

Use this value to retrieve the user record for the user identity. The user record doesn’t contain any personal information about the user, by default. You can add data to the user record, but you shouldn’t add anything sensitive.

## See Also

- [var emailAddress: String?](ckuseridentity/lookupinfo-swift.class/emailaddress.md)
  The user’s email address.
- [var phoneNumber: String?](ckuseridentity/lookupinfo-swift.class/phonenumber.md)
  The user’s phone number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckuseridentity/lookupinfo-swift.class/userrecordid)*