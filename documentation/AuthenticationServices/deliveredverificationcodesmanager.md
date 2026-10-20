# DeliveredVerificationCodesManager

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

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
- [func consumeOneTimeCode(ASVerificationCode) async throws](./deliveredverificationcodesmanager/consumeonetimecode%28_%29.md)
  Mark a one-time code as “consumed” by the current process.
- [func oneTimeCodes(preferredDuration: TimeInterval) async throws -> some AsyncSequence<ASVerificationCode, any Error>
](./deliveredverificationcodesmanager/onetimecodes%28preferredduration%29.md)
  Stream one-time codes received by the system.
### Type Aliases
- [DeliveredVerificationCodesManager.VerificationError](./deliveredverificationcodesmanager/verificationerror.md)

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/deliveredverificationcodesmanager)*