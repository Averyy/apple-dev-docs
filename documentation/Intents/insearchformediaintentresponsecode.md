# INSearchForMediaIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Codes returned by an intents handler in response to a search request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum INSearchForMediaIntentResponseCode
```

```c
enum INSearchForMediaIntentResponseCode : NSInteger;
```

## Topics

### Response Code
- [INSearchForMediaIntentResponseCode.unspecified](./insearchformediaintentresponsecode/unspecified.md)
  An unknown state.
- [INSearchForMediaIntentResponseCode.ready](./insearchformediaintentresponsecode/ready.md)
  The app is ready to perform the search.
- [INSearchForMediaIntentResponseCode.continueInApp](./insearchformediaintentresponsecode/continueinapp.md)
  The system should launch your app in the foreground to search for the media.
- [INSearchForMediaIntentResponseCode.inProgress](./insearchformediaintentresponsecode/inprogress.md)
  The app is currently trying to process the search request.
- [INSearchForMediaIntentResponseCode.success](./insearchformediaintentresponsecode/success.md)
  The app successfully performed the search.
- [INSearchForMediaIntentResponseCode.failure](./insearchformediaintentresponsecode/failure.md)
  The app is unable to search for the media.
- [INSearchForMediaIntentResponseCode.failureRequiringAppLaunch](./insearchformediaintentresponsecode/failurerequiringapplaunch.md)
  The user needs to launch your app to search for the media.
### Initializers
- [init?(rawValue: Int)](./insearchformediaintentresponsecode/init%28rawvalue%29.md)

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
- [var code: INSearchForMediaIntentResponseCode](./insearchformediaintentresponse/code.md)
  A response code that indicates whether the app successfully searched for the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformediaintentresponsecode)*