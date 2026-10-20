# AgeRangeService.Error

**Framework**: Declared Age Range  
**Kind**: enum  
**Role**: Enumeration

An error that occurs when an age range request fails.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
enum Error
```

## Topics

### Interpreting error responses
- [AgeRangeService.Error.notAvailable](./error/notavailable.md)
  Indicates the system was unable to share the person’s age range.
- [AgeRangeService.Error.invalidRequest](./error/invalidrequest.md)
  Indicates your request contains invalid parameters or configuration.
### Enumeration Cases
- [AgeRangeService.Error.declinedOnboarding](./error/declinedonboarding.md)
  Indicates the person declined the age range onboarding flow.
- [AgeRangeService.Error.invalidAccount](./error/invalidaccount.md)
  Indicates the current Apple Account isn’t eligible for age range sharing.
- [AgeRangeService.Error.network](./error/network.md)
  Indicates a network or server issue prevented completing the age range request.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Hashable](../../Swift/hashable.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/error)*