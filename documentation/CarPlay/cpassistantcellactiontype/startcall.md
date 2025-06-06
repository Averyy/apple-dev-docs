# CPAssistantCellActionType.startCall

**Framework**: Carplay  
**Kind**: case

Provides an action that uses Siri to prompt the user for a person, group, or business to call.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
case startCall
```

#### Discussion

> **Note**:  This action is only available in communication apps that include an Intents Extension capable of handling doc://com.apple.documentation/documentation/sirikit/instartcallintent. For more information, see [`Creating an Intents App Extension`](https://developer.apple.com/documentation/SiriKit/creating-an-intents-app-extension).

The system provides the user’s response to your app’s Intents Extension. Your app must respond by identifying the requested person, group, or business and start a voice call with them.

## See Also

- [CPAssistantCellActionType.playMedia](cpassistantcellactiontype/playmedia.md)
  Provides an action that uses Siri to prompt the user for media playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpassistantcellactiontype/startcall)*