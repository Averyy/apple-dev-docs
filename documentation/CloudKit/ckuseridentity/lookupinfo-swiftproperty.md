# lookupInfo

**Framework**: CloudKit  
**Kind**: property

The lookup info for retrieving the user identity.

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
var lookupInfo: CKUserIdentity.LookupInfo? { get }
```

#### Discussion

Use this property’s value to retrieve the user identity when using the [`CKDiscoverUserIdentitiesOperation`](ckdiscoveruseridentitiesoperation.md) and [`CKFetchShareParticipantsOperation`](ckfetchshareparticipantsoperation.md) operations.

## See Also

- [var hasiCloudAccount: Bool](ckuseridentity/hasicloudaccount.md)
  A Boolean value that indicates whether the user has an iCloud account.
- [CKUserIdentity.LookupInfo](ckuseridentity/lookupinfo-swift.class.md)
  The criteria to use when searching for discoverable iCloud users.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckuseridentity/lookupinfo-swift.property)*