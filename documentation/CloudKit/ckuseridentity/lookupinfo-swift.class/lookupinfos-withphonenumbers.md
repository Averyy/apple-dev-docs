# lookupInfos(withPhoneNumbers:)

**Framework**: CloudKit  
**Kind**: method

Returns an array of lookup infos for the specifed phone numbers.

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
class func lookupInfos(withPhoneNumbers phoneNumbers: [String]) -> [CKUserIdentity.LookupInfo]
```

#### Discussion

Use the values that this method returns in an [`CKDiscoverUserIdentitiesOperation`](ckdiscoveruseridentitiesoperation.md) operation or an  [`CKFetchShareParticipantsOperation`](ckfetchshareparticipantsoperation.md) operation to retrieve the corresponding user identities.

## Parameters

- `phoneNumbers`: The phone numbers for looking up the user identities.

## See Also

- [class func lookupInfos(withEmails: [String]) -> [CKUserIdentity.LookupInfo]](ckuseridentity/lookupinfo-swift.class/lookupinfos(withemails:).md)
  Returns an array of lookup infos for the specifed email addresses.
- [class func lookupInfos(with: [CKRecord.ID]) -> [CKUserIdentity.LookupInfo]](ckuseridentity/lookupinfo-swift.class/lookupinfos(with:).md)
  Returns an array of lookup infos for the specifed user record IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckuseridentity/lookupinfo-swift.class/lookupinfos(withphonenumbers:))*