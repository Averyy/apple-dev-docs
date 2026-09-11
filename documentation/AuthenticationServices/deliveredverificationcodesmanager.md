# DeliveredVerificationCodesManager

**Framework**: Authentication Services  
**Kind**: struct

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
struct DeliveredVerificationCodesManager
```

## Topics

### Instance Methods
- [func consumeOneTimeCode(ASVerificationCode) async throws](deliveredverificationcodesmanager/consumeonetimecode(_:).md)
  Mark a one-time code as “consumed” by the current process.
- [func oneTimeCodes(preferredDuration: TimeInterval) async throws -> some AsyncSequence<ASVerificationCode, any Error>
](deliveredverificationcodesmanager/onetimecodes(preferredduration:).md)
  Stream one-time codes received by the system.
### Type Aliases
- [DeliveredVerificationCodesManager.VerificationError](deliveredverificationcodesmanager/verificationerror.md)

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/deliveredverificationcodesmanager)*