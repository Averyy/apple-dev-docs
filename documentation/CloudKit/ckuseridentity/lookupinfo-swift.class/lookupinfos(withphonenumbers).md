# lookupInfos(withPhoneNumbers:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Type Method

Returns an array of lookup infos for the specified phone numbers.

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

```objc
+ (NSArray<CKUserIdentityLookupInfo *> *) lookupInfosWithPhoneNumbers:(NSArray<NSString *> *) phoneNumbers;
```

## Discussion

Use the values that this method returns in an [`CKDiscoverUserIdentitiesOperation`](../../ckdiscoveruseridentitiesoperation.md) operation or an  [`CKFetchShareParticipantsOperation`](../../ckfetchshareparticipantsoperation.md) operation to retrieve the corresponding user identities.

## Parameters

- `phoneNumbers`: The phone numbers for looking up the user identities.

## See Also

### Creating Multiple Lookup Infos
- [class func lookupInfos(withEmails: [String]) -> [CKUserIdentity.LookupInfo]](./lookupinfos%28withemails%29.md)
  Returns an array of lookup infos for the specified email addresses.
- [class func lookupInfos(with: [CKRecord.ID]) -> [CKUserIdentity.LookupInfo]](./lookupinfos%28with%29.md)
  Returns an array of lookup infos for the specified user record IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckuseridentity/lookupinfo-swift.class/lookupinfos(withphonenumbers:))*