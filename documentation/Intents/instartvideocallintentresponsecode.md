# INStartVideoCallIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the status of the response.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: INStartVideoCallIntent is deprecated. Please adopt INStartCallIntent instead

## Declaration

```swift
enum INStartVideoCallIntentResponseCode
```

```c
enum INStartVideoCallIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INStartVideoCallIntentResponseCode.unspecified](./instartvideocallintentresponsecode/unspecified.md)
  Your app can’t provide a more specific response.
- [INStartVideoCallIntentResponseCode.ready](./instartvideocallintentresponsecode/ready.md)
  You’re ready to handle the intent.
- [INStartVideoCallIntentResponseCode.continueInApp](./instartvideocallintentresponsecode/continueinapp.md)
  Your extension is ready to transfer control to the app so that your app can place the call.
- [INStartVideoCallIntentResponseCode.failure](./instartvideocallintentresponsecode/failure.md)
  You were unable to initiate the call.
- [INStartVideoCallIntentResponseCode.failureRequiringAppLaunch](./instartvideocallintentresponsecode/failurerequiringapplaunch.md)
  The user must launch your app to initiate the call.
- [INStartVideoCallIntentResponseCode.failureAppConfigurationRequired](./instartvideocallintentresponsecode/failureappconfigurationrequired.md)
  The user must perform additional configuration steps before initiating a call is possible.
- [INStartVideoCallIntentResponseCode.failureCallingServiceNotAvailable](./instartvideocallintentresponsecode/failurecallingservicenotavailable.md)
  Your app’s calling service isn’t currently available.
- [INStartVideoCallIntentResponseCode.failureContactNotSupportedByApp](./instartvideocallintentresponsecode/failurecontactnotsupportedbyapp.md)
  Your app can’t use the specified contact to place the call.
- [INStartVideoCallIntentResponseCode.failureInvalidNumber](./instartvideocallintentresponsecode/failureinvalidnumber.md)
  The specified number doesn’t support video calls.
### Initializers
- [init?(rawValue: Int)](./instartvideocallintentresponsecode/init%28rawvalue%29.md)

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
- [var code: INStartVideoCallIntentResponseCode](./instartvideocallintentresponse/code.md)
  The code indicating whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartvideocallintentresponsecode)*