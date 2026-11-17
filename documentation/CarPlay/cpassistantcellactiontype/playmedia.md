# CPAssistantCellActionType.playMedia

**Framework**: CarPlay  
**Kind**: case  
**Role**: Case

An option to to play audio or video content.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
case playMedia
```

```c
CPAssistantCellActionTypePlayMedia
```

## Discussion

To respond to this action, make sure your app implements an Intents extension capable of handling the [`INPlayMediaIntent`](../../Intents/inplaymediaintent.md) type. When someone chooses this action, Siri prompts the person to specify the media item to play and passes that information to your app extension. Use the information to locate the specified media item, start playback, and display the [`CPNowPlayingTemplate`](../cpnowplayingtemplate.md).

> **Note**: This action is available only to audio or video apps.

For more information about how to implement an Intents extension, see [Creating an Intents App Extension](../../SiriKit/creating-an-intents-app-extension.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpassistantcellactiontype/playmedia)*