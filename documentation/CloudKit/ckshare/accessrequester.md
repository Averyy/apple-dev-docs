# CKShare.AccessRequester

**Framework**: CloudKit  
**Kind**: class

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
class AccessRequester
```

## Topics

### Instance Properties
- [var contact: CNContact](ckshare/accessrequester/contact.md)
  Returns a displayable `CNContact` for the requester, or a new `CNContact` if none exists in the user’s contacts. Provides a standardized format for the requester’s underlying lookup info in the user identity. Use when displaying the requester information to other participants and approvers in application UI.
- [var participantLookupInfo: CKUserIdentity.LookupInfo](ckshare/accessrequester/participantlookupinfo.md)
  Convenience method to get the requester’s lookup info. This lookup info can be used in [`CKFetchShareParticipantsOperation`](ckfetchshareparticipantsoperation.md) to approve the requester by fetching the corresponding participant and adding the participant to the share.
- [var userIdentity: CKUserIdentity](ckshare/accessrequester/useridentity.md)
  The user identity this share access requester represents.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/accessrequester)*