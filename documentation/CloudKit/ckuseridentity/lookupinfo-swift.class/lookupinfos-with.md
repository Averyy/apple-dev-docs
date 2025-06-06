# lookupInfos(with:)

**Framework**: CloudKit  
**Kind**: method

Returns an array of lookup infos for the specifed user record IDs.

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
class func lookupInfos(with recordIDs: [CKRecord.ID]) -> [CKUserIdentity.LookupInfo]
```

#### Discussion

Use the values that this method returns in an [`CKDiscoverUserIdentitiesOperation`](ckdiscoveruseridentitiesoperation.md) operation or an  [`CKFetchShareParticipantsOperation`](ckfetchshareparticipantsoperation.md) operation to retrieve the corresponding user identities.

## Parameters

- `recordIDs`: The user record IDs for looking up the user identities.

## See Also

- [class func lookupInfos(withEmails: [String]) -> [CKUserIdentity.LookupInfo]](ckuseridentity/lookupinfo-swift.class/lookupinfos(withemails:).md)
  Returns an array of lookup infos for the specifed email addresses.
- [class func lookupInfos(withPhoneNumbers: [String]) -> [CKUserIdentity.LookupInfo]](ckuseridentity/lookupinfo-swift.class/lookupinfos(withphonenumbers:).md)
  Returns an array of lookup infos for the specifed phone numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckuseridentity/lookupinfo-swift.class/lookupinfos(with:))*