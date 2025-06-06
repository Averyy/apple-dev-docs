# userIdentityLookupInfos

**Framework**: CloudKit  
**Kind**: property

The user data for the participants.

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
var userIdentityLookupInfos: [CKUserIdentity.LookupInfo]? { get set }
```

#### Discussion

Use this property to view or change the participants user data. If you intend to specify or change the value of this property, do so before you execute the operation or submit it to a queue.

> **Note**:  If you don’t set [`userIdentityLookupInfos`](ckfetchshareparticipantsoperation/useridentitylookupinfos.md) prior to executing the operation, it returns immediately with no results.

 If you don’t set [`userIdentityLookupInfos`](ckfetchshareparticipantsoperation/useridentitylookupinfos.md) prior to executing the operation, it returns immediately with no results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchshareparticipantsoperation/useridentitylookupinfos)*