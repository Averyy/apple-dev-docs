# AgeRangeService.Error

**Framework**: Declared Age Range  
**Kind**: enum

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
- [AgeRangeService.Error.notAvailable](agerangeservice/error/notavailable.md)
  Indicates the system was unable to share the person’s age range.
- [AgeRangeService.Error.invalidRequest](agerangeservice/error/invalidrequest.md)
  Indicates your request contains invalid parameters or configuration.
### Enumeration Cases
- [AgeRangeService.Error.declinedOnboarding](agerangeservice/error/declinedonboarding.md)
  Indicates the person declined the age range onboarding flow.
- [AgeRangeService.Error.invalidAccount](agerangeservice/error/invalidaccount.md)
  Indicates the current Apple Account isn’t eligible for age range sharing.
- [AgeRangeService.Error.network](agerangeservice/error/network.md)
  Indicates a network or server issue prevented completing the age range request.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Error](../swift/error.md)
- [Hashable](../swift/hashable.md)
- [LocalizedError](../foundation/localizederror.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/error)*