# INSetClimateSettingsInCarIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the state of the response.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
enum INSetClimateSettingsInCarIntentResponseCode
```

```c
enum INSetClimateSettingsInCarIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INSetClimateSettingsInCarIntentResponseCode.unspecified](./insetclimatesettingsincarintentresponsecode/unspecified.md)
  The response didn’t specify a resonse code.
- [INSetClimateSettingsInCarIntentResponseCode.ready](./insetclimatesettingsincarintentresponsecode/ready.md)
  You’re ready to handle the intent.
- [INSetClimateSettingsInCarIntentResponseCode.inProgress](./insetclimatesettingsincarintentresponsecode/inprogress.md)
  You’re in the process of handling the intent.
- [INSetClimateSettingsInCarIntentResponseCode.success](./insetclimatesettingsincarintentresponsecode/success.md)
  You successfully handled the intent.
- [INSetClimateSettingsInCarIntentResponseCode.failure](./insetclimatesettingsincarintentresponsecode/failure.md)
  You were unable to change the climate control settings.
- [INSetClimateSettingsInCarIntentResponseCode.failureRequiringAppLaunch](./insetclimatesettingsincarintentresponsecode/failurerequiringapplaunch.md)
  The user must launch your app to change the climate control settings.
### Initializers
- [init?(rawValue: Int)](./insetclimatesettingsincarintentresponsecode/init%28rawvalue%29.md)

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
- [var code: INSetClimateSettingsInCarIntentResponseCode](./insetclimatesettingsincarintentresponse/code.md)
  The code indicating whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetclimatesettingsincarintentresponsecode)*