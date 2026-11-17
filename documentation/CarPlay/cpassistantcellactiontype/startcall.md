# CPAssistantCellActionType.startCall

**Framework**: CarPlay  
**Kind**: case  
**Role**: Case

An option to call a person, group, or business.

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

## Discussion

To respond to this action, make sure your app implements an Intents extension capable of handling the [`INStartCallIntent`](../../Intents/instartcallintent.md) type. When someone chooses this action, Siri prompts the person to specify the person, group, or business to call. Use the information to locate the appropriate contact details and start a voice call.

> **Note**: This action is available only to communication apps.

For more information about how to implement an Intents extension, see [Creating an Intents App Extension](../../SiriKit/creating-an-intents-app-extension.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpassistantcellactiontype/startcall)*