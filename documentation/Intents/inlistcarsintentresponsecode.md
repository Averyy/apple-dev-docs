# INListCarsIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that represent the status of a response.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
enum INListCarsIntentResponseCode
```

```c
enum INListCarsIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INListCarsIntentResponseCode.failure](./inlistcarsintentresponsecode/failure.md)
  A response code that indicates you’re unable to retrieve a list of the user’s electric vehicles.
- [INListCarsIntentResponseCode.failureRequiringAppLaunch](./inlistcarsintentresponsecode/failurerequiringapplaunch.md)
  A response code that indicates the system must launch your app before you can provide a list of the user’s electric vehicles.
- [INListCarsIntentResponseCode.inProgress](./inlistcarsintentresponsecode/inprogress.md)
  A response code that indicates you’re in the process of retrieving a list of the user’s electric vehicles, but they are not yet available.
- [INListCarsIntentResponseCode.ready](./inlistcarsintentresponsecode/ready.md)
  A response code that indicates you’re ready to provide a list of the user’s electric vehicles.
- [INListCarsIntentResponseCode.success](./inlistcarsintentresponsecode/success.md)
  A response code that indicates you’re able to provide a list of the user’s electric vehicles.
- [INListCarsIntentResponseCode.unspecified](./inlistcarsintentresponsecode/unspecified.md)
  A response code that indicates the absence of a genuine response code.
### Initializers
- [init?(rawValue: Int)](./inlistcarsintentresponsecode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Response Code
- [var code: INListCarsIntentResponseCode](./inlistcarsintentresponse/code.md)
  The code that indicates success or failure when confirming or handling the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistcarsintentresponsecode)*