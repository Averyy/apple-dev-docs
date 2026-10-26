# INUpdateMediaAffinityIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Codes returned by an intents handler in response to an update media affinity request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum INUpdateMediaAffinityIntentResponseCode
```

```c
enum INUpdateMediaAffinityIntentResponseCode : NSInteger;
```

## Topics

### Response Code
- [INUpdateMediaAffinityIntentResponseCode.unspecified](./inupdatemediaaffinityintentresponsecode/unspecified.md)
  An unknown state.
- [INUpdateMediaAffinityIntentResponseCode.ready](./inupdatemediaaffinityintentresponsecode/ready.md)
  The app is ready.
- [INUpdateMediaAffinityIntentResponseCode.inProgress](./inupdatemediaaffinityintentresponsecode/inprogress.md)
  The app is currently trying to process the update affinity request.
- [INUpdateMediaAffinityIntentResponseCode.success](./inupdatemediaaffinityintentresponsecode/success.md)
  The app successfully updated the user’s affinity for the media.
- [INUpdateMediaAffinityIntentResponseCode.failure](./inupdatemediaaffinityintentresponsecode/failure.md)
  The app is unable to update the user’s affinity for the media.
- [INUpdateMediaAffinityIntentResponseCode.failureRequiringAppLaunch](./inupdatemediaaffinityintentresponsecode/failurerequiringapplaunch.md)
  The user needs to launch the app to update the user’s affinity for the media.
### Initializers
- [init?(rawValue: Int)](./inupdatemediaaffinityintentresponsecode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Providing the Response Code
- [var code: INUpdateMediaAffinityIntentResponseCode](./inupdatemediaaffinityintentresponse/code.md)
  The code that indicates whether the app successfully updated the user’s affinity for the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inupdatemediaaffinityintentresponsecode)*