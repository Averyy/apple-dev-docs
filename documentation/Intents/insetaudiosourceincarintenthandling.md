# INSetAudioSourceInCarIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for changing a vehicle’s audio source.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
protocol INSetAudioSourceInCarIntentHandling : NSObjectProtocol
```

```objc
@protocol INSetAudioSourceInCarIntentHandling <NSObject>
```

## Overview

Automotive venders can support the [`INSetAudioSourceInCarIntentHandling`](./insetaudiosourceincarintenthandling.md) protocol in an Intents extension that they ship with their automotive apps. Use the methods of this protocol to resolve, confirm, and handle requests to change the vehicle’s current audio source. Your extension should be able to communicate with the vehicle and make the necessary audio changes.

Siri delivers an [`INSetAudioSourceInCarIntent`](./insetaudiosourceincarintent.md) object to your handler when the user asks to change the audio source. The provided intent object contains information that you use to determine the new audio source and to make the change.

## Topics

### Resolving the Intent Parameters
- [func resolveAudioSource(for: INSetAudioSourceInCarIntent, with: (INCarAudioSourceResolutionResult) -> Void)](./insetaudiosourceincarintenthandling/resolveaudiosource%28for,with%29.md)
  Resolves an explicitly selected audio source.
- [func resolveRelativeAudioSourceReference(for: INSetAudioSourceInCarIntent, with: (INRelativeReferenceResolutionResult) -> Void)](./insetaudiosourceincarintenthandling/resolverelativeaudiosourcereference%28for,with%29.md)
  Resolves the audio source using a relative qualifier.
### Confirming the Response
- [func confirm(intent: INSetAudioSourceInCarIntent, completion: (INSetAudioSourceInCarIntentResponse) -> Void)](./insetaudiosourceincarintenthandling/confirm%28intent,completion%29.md)
  Confirms whether you can change the audio source.
### Handling the Intent
- [func handle(intent: INSetAudioSourceInCarIntent, completion: (INSetAudioSourceInCarIntentResponse) -> Void)](./insetaudiosourceincarintenthandling/handle%28intent,completion%29.md)
  Handles changing the audio source.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INCarPlayDomainHandling](./incarplaydomainhandling.md)

## See Also

### CarPlay Audio Source
- [class INSetAudioSourceInCarIntent](./insetaudiosourceincarintent.md)
  A request to change the source of audio playback in a CarPlay-enabled vehicle.
- [class INSetAudioSourceInCarIntentResponse](./insetaudiosourceincarintentresponse.md)
  Your app’s response to a set audio source in car intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetaudiosourceincarintenthandling)*