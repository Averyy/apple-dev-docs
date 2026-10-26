# INActivateCarSignalIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the status of the response.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
enum INActivateCarSignalIntentResponseCode
```

```c
enum INActivateCarSignalIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INActivateCarSignalIntentResponseCode.failure](./inactivatecarsignalintentresponsecode/failure.md)
  An error code indicating that you were unable to activate the car’s signals.
- [INActivateCarSignalIntentResponseCode.failureRequiringAppLaunch](./inactivatecarsignalintentresponsecode/failurerequiringapplaunch.md)
  An error code indicating that the user must launch your app to activate the car’s signals.
- [INActivateCarSignalIntentResponseCode.inProgress](./inactivatecarsignalintentresponsecode/inprogress.md)
  A response code indicating that you are activating the signals but do not yet have the results.
- [INActivateCarSignalIntentResponseCode.ready](./inactivatecarsignalintentresponsecode/ready.md)
  A response code indicating that you are ready to handle the intent.
- [INActivateCarSignalIntentResponseCode.success](./inactivatecarsignalintentresponsecode/success.md)
  A response code indicating that you have successfully handled the intent.
- [INActivateCarSignalIntentResponseCode.unspecified](./inactivatecarsignalintentresponsecode/unspecified.md)
  A response code indicating that the status was not specified.
### Initializers
- [init?(rawValue: Int)](./inactivatecarsignalintentresponsecode/init%28rawvalue%29.md)

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
- [var code: INActivateCarSignalIntentResponseCode](./inactivatecarsignalintentresponse/code.md)
  The code indicating success or failure when confirming or handling an intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inactivatecarsignalintentresponsecode)*