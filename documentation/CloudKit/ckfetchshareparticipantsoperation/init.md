# init()

**Framework**: CloudKit  
**Kind**: init

Creates an empty operation.

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
init()
```

#### Discussion

You can use this operation only once.

> **Note**:  If you don’t set [`userIdentityLookupInfos`](ckfetchshareparticipantsoperation/useridentitylookupinfos.md) prior to executing the operation, it returns immediately with no results.

 If you don’t set [`userIdentityLookupInfos`](ckfetchshareparticipantsoperation/useridentitylookupinfos.md) prior to executing the operation, it returns immediately with no results.

## See Also

- [convenience init(userIdentityLookupInfos: [CKUserIdentity.LookupInfo])](ckfetchshareparticipantsoperation/init(useridentitylookupinfos:).md)
  Creates an operation for generating share participants from the specified user data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchshareparticipantsoperation/init())*