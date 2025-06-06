# userIdentityLookupInfos

**Framework**: CloudKit  
**Kind**: property

The lookup info for discovering user identities.

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
var userIdentityLookupInfos: [CKUserIdentity.LookupInfo] { get set }
```

#### Discussion

Use this property to view or change the lookup info that CloudKit uses to discover user identities. If you intend to modify this property’s value, do so before you execute the operation or submit it to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdiscoveruseridentitiesoperation/useridentitylookupinfos)*