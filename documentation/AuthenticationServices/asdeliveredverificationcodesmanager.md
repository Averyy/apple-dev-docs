# ASDeliveredVerificationCodesManager

**Framework**: Authentication Services  
**Kind**: class

This class allows interacting with one-time codes delivered to the system.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class ASDeliveredVerificationCodesManager
```

#### Overview

The codes may be delivered from many different sources, for example, email or SMS.

## Topics

### Structures
- [ASDeliveredVerificationCodesManager.VerificationError](asdeliveredverificationcodesmanager/verificationerror.md)
### Initializers
- [init()](asdeliveredverificationcodesmanager/init.md)
### Instance Methods
- [func consumeOneTimeCode(ASVerificationCode) async throws](asdeliveredverificationcodesmanager/consumeonetimecode(_:).md)
  Mark a one-time code as “consumed” by the current process.
- [func oneTimeCodes(preferredDuration: TimeInterval, anchor: ASPresentationAnchor) async throws -> some AsyncSequence<ASVerificationCode, any Error>
](asdeliveredverificationcodesmanager/onetimecodes(preferredduration:anchor:)-6x2k6.md)
  Stream one-time codes received by the system.
- [func oneTimeCodes(preferredDuration: TimeInterval, anchor: ASPresentationAnchor) async throws -> some AsyncSequence<ASVerificationCode, any Error>
](asdeliveredverificationcodesmanager/onetimecodes(preferredduration:anchor:)-tyrg.md)
  Stream one-time codes received by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asdeliveredverificationcodesmanager)*