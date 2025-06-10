# CKShare.BlockedIdentity

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
class BlockedIdentity
```

## Topics

### Instance Properties
- [var contact: CNContact](ckshare/blockedidentity/contact.md)
  Returns a displayable `CNContact` for the blocked identity, or a new `CNContact` if none exists in the user’s contacts. Provides a standardized format for the blocked identity’s underlying lookup info in the user identity. Use when displaying the blocked identity information to other participants in application UI.
- [var userIdentity: CKUserIdentity](ckshare/blockedidentity/useridentity.md)
  The user identity this blocked identity represents.

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

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/blockedidentity)*