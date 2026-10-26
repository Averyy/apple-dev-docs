# INPlayMediaIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Codes returned by an app or Intents app extension when handling or confirming a play media intent.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
enum INPlayMediaIntentResponseCode
```

```c
enum INPlayMediaIntentResponseCode : NSInteger;
```

## Topics

### Intents App Extensions
- [INPlayMediaIntentResponseCode.ready](./inplaymediaintentresponsecode/ready.md)
  The intents handler is ready to handle the intent.
- [INPlayMediaIntentResponseCode.continueInApp](./inplaymediaintentresponsecode/continueinapp.md)
  The system should launch the app in the foreground to play the media.
- [INPlayMediaIntentResponseCode.handleInApp](./inplaymediaintentresponsecode/handleinapp.md)
  The system should launch the app in the background to play the media.
### App
- [INPlayMediaIntentResponseCode.inProgress](./inplaymediaintentresponsecode/inprogress.md)
  The app is preparing to play the media content.
- [INPlayMediaIntentResponseCode.success](./inplaymediaintentresponsecode/success.md)
  The app is playing the media.
### General
- [INPlayMediaIntentResponseCode.unspecified](./inplaymediaintentresponsecode/unspecified.md)
  An unspecified response code.
### Failures
- [INPlayMediaIntentResponseCode.failure](./inplaymediaintentresponsecode/failure.md)
  A failure occurred while confirming or handling the intent.
- [INPlayMediaIntentResponseCode.failureNoUnplayedContent](./inplaymediaintentresponsecode/failurenounplayedcontent.md)
  The media container has no unplayed content.
- [INPlayMediaIntentResponseCode.failureRequiringAppLaunch](./inplaymediaintentresponsecode/failurerequiringapplaunch.md)
  The user must launch the app before media playback can begin.
- [INPlayMediaIntentResponseCode.failureRestrictedContent](./inplaymediaintentresponsecode/failurerestrictedcontent.md)
  The app cannot play the media because of content restrictions.
- [INPlayMediaIntentResponseCode.failureUnknownMediaType](./inplaymediaintentresponsecode/failureunknownmediatype.md)
  The app cannot play the media because the type is unknown or not supported.
### Enumeration Cases
- [INPlayMediaIntentResponseCode.failureMaxStreamLimitReached](./inplaymediaintentresponsecode/failuremaxstreamlimitreached.md)
### Initializers
- [init?(rawValue: Int)](./inplaymediaintentresponsecode/init%28rawvalue%29.md)

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
- [var code: INPlayMediaIntentResponseCode](./inplaymediaintentresponse/code.md)
  A response code that indicates whether the app can play the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediaintentresponsecode)*