# INStartAudioCallIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the status of the response.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 6.0

> **Deprecated**: INStartAudioCallIntent is deprecated. Please adopt INStartCallIntent instead

## Declaration

```swift
enum INStartAudioCallIntentResponseCode
```

```c
enum INStartAudioCallIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INStartAudioCallIntentResponseCode.unspecified](./instartaudiocallintentresponsecode/unspecified.md)
  Your app can’t provide a specific status.
- [INStartAudioCallIntentResponseCode.ready](./instartaudiocallintentresponsecode/ready.md)
  You’re ready to handle the intent.
- [INStartAudioCallIntentResponseCode.continueInApp](./instartaudiocallintentresponsecode/continueinapp.md)
  Your extension is ready to transfer control so your app can place the call.
- [INStartAudioCallIntentResponseCode.failure](./instartaudiocallintentresponsecode/failure.md)
  You were unable to initiate the call.
- [INStartAudioCallIntentResponseCode.failureRequiringAppLaunch](./instartaudiocallintentresponsecode/failurerequiringapplaunch.md)
  The user must launch your app to initiate the call.
- [INStartAudioCallIntentResponseCode.failureAppConfigurationRequired](./instartaudiocallintentresponsecode/failureappconfigurationrequired.md)
  The user must perform additional configuration steps before initiating a call is possible.
- [INStartAudioCallIntentResponseCode.failureCallingServiceNotAvailable](./instartaudiocallintentresponsecode/failurecallingservicenotavailable.md)
  Your app’s calling service isn’t currently available.
- [INStartAudioCallIntentResponseCode.failureContactNotSupportedByApp](./instartaudiocallintentresponsecode/failurecontactnotsupportedbyapp.md)
  You can’t use the specified contact to place the call.
- [INStartAudioCallIntentResponseCode.failureNoValidNumber](./instartaudiocallintentresponsecode/failurenovalidnumber.md)
  The specified number doesn’t support audio calls.
### Initializers
- [init?(rawValue: Int)](./instartaudiocallintentresponsecode/init%28rawvalue%29.md)

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
- [var code: INStartAudioCallIntentResponseCode](./instartaudiocallintentresponse/code.md)
  The code indicating whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartaudiocallintentresponsecode)*