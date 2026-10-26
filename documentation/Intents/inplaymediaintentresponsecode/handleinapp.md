# INPlayMediaIntentResponseCode.handleInApp

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The system should launch the app in the background to play the media.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case handleInApp
```

```c
INPlayMediaIntentResponseCodeHandleInApp
```

## Mentions

- [Improving Siri Media Interactions and App Selection](../../SiriKit/improving-siri-media-interactions-and-app-selection.md)

#### Discussion

Because the lifespan of an app extension is short, media playback should happen in your app, not in the Intents app extension. To handle media playback in your app while in the background, return [`INPlayMediaIntentResponseCode.handleInApp`](./handleinapp.md) as the response [`code`](../inplaymediaintentresponse/code.md).

## See Also

### Intents App Extensions
- [INPlayMediaIntentResponseCode.ready](./ready.md)
  The intents handler is ready to handle the intent.
- [INPlayMediaIntentResponseCode.continueInApp](./continueinapp.md)
  The system should launch the app in the foreground to play the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediaintentresponsecode/handleinapp)*