# userIdentityLookupInfos

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The lookup info for discovering user identities.

**Availability**:
- iOS 10.0+ - Deprecated in 17.0
- iPadOS 10.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- macOS 10.12+ - Deprecated in 14.0
- tvOS 10.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 10.0

> **Deprecated**: No longer supported. Please see Sharing CloudKit Data with Other iCloud Users.

## Declaration

```swift
var userIdentityLookupInfos: [CKUserIdentity.LookupInfo] { get set }
```

```objc
@property (nonatomic, copy) NSArray<CKUserIdentityLookupInfo *> * userIdentityLookupInfos;
```

#### Discussion

Use this property to view or change the lookup info that CloudKit uses to discover user identities. If you intend to modify this property’s value, do so before you execute the operation or submit it to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdiscoveruseridentitiesoperation/useridentitylookupinfos)*