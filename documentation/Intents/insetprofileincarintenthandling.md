# INSetProfileInCarIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for restoring vehicle environment settings from a user-specified profile.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
protocol INSetProfileInCarIntentHandling : NSObjectProtocol
```

```objc
@protocol INSetProfileInCarIntentHandling <NSObject>
```

## Overview

Automotive venders can support the [`INSetProfileInCarIntentHandling`](./insetprofileincarintenthandling.md) protocol in an Intents extension that they ship with their automotive apps. Use the methods of this protocol to resolve, confirm, and handle requests to restore vehicle-related settings from the profile that the user designated. Your extension should be able to communicate with the vehicle and make the necessary changes.

Siri delivers an [`INSetProfileInCarIntent`](./insetprofileincarintent.md) object to your handler when the user asks to restore the current settings from a profile. The provided intent object contains information for determining which profile to use.

## Topics

### Resolving the Intent Parameters
- [func resolveProfileNumber(for: INSetProfileInCarIntent, with: (INIntegerResolutionResult) -> Void)](./insetprofileincarintenthandling/resolveprofilenumber%28for,with%29.md)
  Resolves the profile index from which to restore any settings.
- [func resolveProfileName(for: INSetProfileInCarIntent, with: (INStringResolutionResult) -> Void)](./insetprofileincarintenthandling/resolveprofilename%28for,with%29.md)
  Resolves the profile name from which to retrieve settings.
- [func resolveCarName(for: INSetProfileInCarIntent, with: (INSpeakableStringResolutionResult) -> Void)](./insetprofileincarintenthandling/resolvecarname%28for,with%29.md)
  Resolves the car name.
- [func resolveDefaultProfile(forSetProfileInCar: INSetProfileInCarIntent, with: (INBooleanResolutionResult) -> Void)](./insetprofileincarintenthandling/resolvedefaultprofile%28forsetprofileincar,with%29.md)
  Resolves whether the profile can become the default profile.
### Confirming the Response
- [func confirm(intent: INSetProfileInCarIntent, completion: (INSetProfileInCarIntentResponse) -> Void)](./insetprofileincarintenthandling/confirm%28intent,completion%29.md)
  Confirms whether you can restore the settings from the designated profile.
### Handling the Intent
- [func handle(intent: INSetProfileInCarIntent, completion: (INSetProfileInCarIntentResponse) -> Void)](./insetprofileincarintenthandling/handle%28intent,completion%29.md)
  Handles restoring settings from the designated profile.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INCarPlayDomainHandling](./incarplaydomainhandling.md)

## See Also

### CarPlay Profile Settings
- [class INSetProfileInCarIntent](./insetprofileincarintent.md)
  A request to change the user’s vehicle environment settings to the ones from the specified profile.
- [class INSetProfileInCarIntentResponse](./insetprofileincarintentresponse.md)
  Your app’s response to a set profile in car intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetprofileincarintenthandling)*