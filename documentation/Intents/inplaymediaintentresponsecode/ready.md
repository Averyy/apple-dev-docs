# INPlayMediaIntentResponseCode.ready

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The intents handler is ready to handle the intent.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
case ready
```

```c
INPlayMediaIntentResponseCodeReady
```

#### Discussion

Respond with this code in your Intents app extension’s [`confirm(intent:completion:)`](../inplaymediaintenthandling/confirm%28intent,completion%29.md) method after verifying that your app can play the requested media.

## See Also

### Intents App Extensions
- [INPlayMediaIntentResponseCode.continueInApp](./continueinapp.md)
  The system should launch the app in the foreground to play the media.
- [INPlayMediaIntentResponseCode.handleInApp](./handleinapp.md)
  The system should launch the app in the background to play the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediaintentresponsecode/ready)*