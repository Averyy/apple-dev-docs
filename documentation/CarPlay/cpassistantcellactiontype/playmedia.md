# CPAssistantCellActionType.playMedia

**Framework**: CarPlay  
**Kind**: case

Provides an action that uses Siri to prompt the user for media playback.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
case playMedia
```

#### Discussion

> **Note**:  This action is only available in audio apps that include an Intents Extension capable of handling doc://com.apple.documentation/documentation/sirikit/inplaymediaintent. For more information, see [`Creating an Intents App Extension`](https://developer.apple.com/documentation/SiriKit/creating-an-intents-app-extension).

 This action is only available in audio apps that include an Intents Extension capable of handling doc://com.apple.documentation/documentation/sirikit/inplaymediaintent. For more information, see [`Creating an Intents App Extension`](https://developer.apple.com/documentation/SiriKit/creating-an-intents-app-extension).

The system provides the user’s response to your app’s Intents Extension. Your app must respond by searching for the requested media and, if it’s available, start its playback and display a [`CPNowPlayingTemplate`](cpnowplayingtemplate.md).

## See Also

- [CPAssistantCellActionType.startCall](cpassistantcellactiontype/startcall.md)
  Provides an action that uses Siri to prompt the user for a person, group, or business to call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpassistantcellactiontype/playmedia)*