# ASSavePasswordRequest.Event

**Framework**: Authentication Services  
**Kind**: enum

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- visionOS 26.2+

## Declaration

```swift
enum Event
```

## Topics

### Enumeration Cases
- [ASSavePasswordRequest.Event.formDidDisappear](assavepasswordrequest/event-swift.enum/formdiddisappear.md)
  The save event that occurs when a form is submitted or removed from the screen without prompting the user.
- [ASSavePasswordRequest.Event.generatedPasswordFilled](assavepasswordrequest/event-swift.enum/generatedpasswordfilled.md)
  A save event that occurs when generated password is filled into a not yet submitted form.
- [ASSavePasswordRequest.Event.userInitiated](assavepasswordrequest/event-swift.enum/userinitiated.md)
  The save event that occurs when a user has expressly stated they wish to save the credential.
### Initializers
- [init?(rawValue: Int)](assavepasswordrequest/event-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/assavepasswordrequest/event-swift.enum)*