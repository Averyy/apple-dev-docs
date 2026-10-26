# INAddMediaIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Codes returned by an app or Intents app extension when handling or confirming an add media intent.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum INAddMediaIntentResponseCode
```

```c
enum INAddMediaIntentResponseCode : NSInteger;
```

## Topics

### Response Code
- [INAddMediaIntentResponseCode.unspecified](./inaddmediaintentresponsecode/unspecified.md)
  An unknown state.
- [INAddMediaIntentResponseCode.ready](./inaddmediaintentresponsecode/ready.md)
  The app is ready to add media.
- [INAddMediaIntentResponseCode.inProgress](./inaddmediaintentresponsecode/inprogress.md)
  The app is currently trying to process the add media request.
- [INAddMediaIntentResponseCode.success](./inaddmediaintentresponsecode/success.md)
  The app successfully added the media.
- [INAddMediaIntentResponseCode.handleInApp](./inaddmediaintentresponsecode/handleinapp.md)
  The system should launch the app in the background to handle the intent.
- [INAddMediaIntentResponseCode.failure](./inaddmediaintentresponsecode/failure.md)
  The app was unable to add the media.
- [INAddMediaIntentResponseCode.failureRequiringAppLaunch](./inaddmediaintentresponsecode/failurerequiringapplaunch.md)
  The user must launch the app to add media.
### Initializers
- [init?(rawValue: Int)](./inaddmediaintentresponsecode/init%28rawvalue%29.md)

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
- [var code: INAddMediaIntentResponseCode](./inaddmediaintentresponse/code.md)
  A response code that indicates whether the app successfully added the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddmediaintentresponsecode)*