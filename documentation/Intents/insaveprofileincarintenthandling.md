# INSaveProfileInCarIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for saving vehicle environment settings to a user-specified profile.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
protocol INSaveProfileInCarIntentHandling : NSObjectProtocol
```

```objc
@protocol INSaveProfileInCarIntentHandling <NSObject>
```

#### Overview

Automotive vendors can support the [`INSaveProfileInCarIntentHandling`](./insaveprofileincarintenthandling.md) protocol in an Intents extension that they ship with their automotive apps. Use the methods of this protocol to resolve, confirm, and handle requests to save vehicle-related settings to the profile that the user designated. Your extension should be able to communicate with the vehicle and save the necessary settings.

Siri delivers an [`INSaveProfileInCarIntent`](./insaveprofileincarintent.md) object to your handler when the user asks to save the current settings to a specific profile. The provided intent object contains information that you use to determine where to save the settings.

## Topics

### Resolving the Intent Parameters
- [func resolveProfileNumber(for: INSaveProfileInCarIntent, with: (INIntegerResolutionResult) -> Void)](./insaveprofileincarintenthandling/resolveprofilenumber%28for,with%29.md)
  Resolves the profile index in which to save any settings.
- [func resolveProfileName(for: INSaveProfileInCarIntent, with: (INStringResolutionResult) -> Void)](./insaveprofileincarintenthandling/resolveprofilename%28for,with%29.md)
  Resolves the profile name in which to save any settings.
### Confirming the Response
- [func confirm(intent: INSaveProfileInCarIntent, completion: (INSaveProfileInCarIntentResponse) -> Void)](./insaveprofileincarintenthandling/confirm%28intent,completion%29.md)
  Confirms whether you can save the settings to the designated profile.
### Handling the Intent
- [func handle(intent: INSaveProfileInCarIntent, completion: (INSaveProfileInCarIntentResponse) -> Void)](./insaveprofileincarintenthandling/handle%28intent,completion%29.md)
  Handles saving any settings to the designated profile.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INCarPlayDomainHandling](./incarplaydomainhandling.md)

## See Also

### CarPlay Profile Saving
- [class INSaveProfileInCarIntent](./insaveprofileincarintent.md)
  A request to save the user’s vehicle environment settings in a CarPlay-enabled vehicle.
- [class INSaveProfileInCarIntentResponse](./insaveprofileincarintentresponse.md)
  Your app’s response to a save profile in car intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insaveprofileincarintenthandling)*