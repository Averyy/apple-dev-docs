# ASSavePasswordRequest.Event

**Framework**: Authentication Services  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- visionOS 26.2+

## Declaration

```swift
enum Event
```

```c
enum ASSavePasswordRequestEvent : NSInteger;
```

## Topics

### Enumeration Cases
- [ASSavePasswordRequest.Event.formDidDisappear](./event-swift.enum/formdiddisappear.md)
  The save event that occurs when a form is submitted or removed from the screen without prompting the user.
- [ASSavePasswordRequest.Event.generatedPasswordFilled](./event-swift.enum/generatedpasswordfilled.md)
  A save event that occurs when generated password is filled into a not yet submitted form.
- [ASSavePasswordRequest.Event.userInitiated](./event-swift.enum/userinitiated.md)
  The save event that occurs when a user has expressly stated they wish to save the credential.
### Initializers
- [init?(rawValue: Int)](./event-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/assavepasswordrequest/event-swift.enum)*