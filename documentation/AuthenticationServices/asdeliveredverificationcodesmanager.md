# ASDeliveredVerificationCodesManager

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

This class allows interacting with one-time codes delivered to the system.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
class ASDeliveredVerificationCodesManager
```

#### Overview

The codes may be delivered from many different sources, for example, email or SMS.

## Topics

### Structures
- [ASDeliveredVerificationCodesManager.VerificationError](./asdeliveredverificationcodesmanager/verificationerror.md)
### Initializers
- [init()](./asdeliveredverificationcodesmanager/init%28%29.md)
### Instance Methods
- [func consumeOneTimeCode(ASVerificationCode) async throws](./asdeliveredverificationcodesmanager/consumeonetimecode%28_%29.md)
  Mark a one-time code as “consumed” by the current process.
- [func oneTimeCodes(preferredDuration: TimeInterval, anchor: ASPresentationAnchor) async throws -> some AsyncSequence<ASVerificationCode, any Error>
](./asdeliveredverificationcodesmanager/onetimecodes%28preferredduration,anchor%29-6x2k6.md)
  Stream one-time codes received by the system.
- [func oneTimeCodes(preferredDuration: TimeInterval, anchor: ASPresentationAnchor) async throws -> some AsyncSequence<ASVerificationCode, any Error>
](./asdeliveredverificationcodesmanager/onetimecodes%28preferredduration,anchor%29-tyrg.md)
  Stream one-time codes received by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asdeliveredverificationcodesmanager)*