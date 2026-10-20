# CPAssistantCellActionType.startCall

**Framework**: CarPlay  
**Kind**: case  
**Role**: Case

Provides an action that uses Siri to prompt the user for a person, group, or business to call.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
case startCall
```

```c
CPAssistantCellActionTypeStartCall
```

#### Discussion

> **Note**:  This action is only available in communication apps that include an Intents Extension capable of handling [`INStartCallIntent`](https://developer.apple.com/documentation/intents/instartcallintent). For more information, see [Creating an Intents App Extension](../../SiriKit/creating-an-intents-app-extension.md).

The system provides the user’s response to your app’s Intents Extension. Your app must respond by identifying the requested person, group, or business and start a voice call with them.

## See Also

### Siri Actions
- [CPAssistantCellActionType.playMedia](./playmedia.md)
  Provides an action that uses Siri to prompt the user for media playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpassistantcellactiontype/startcall)*