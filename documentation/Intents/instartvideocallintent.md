# INStartVideoCallIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to start a video call with one or more users.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`INStartCallIntent`](./instartcallintent.md) instead.

## Declaration

```swift
class INStartVideoCallIntent
```

```objc
@interface INStartVideoCallIntent : INIntent
```

#### Overview

The system creates `INStartVideoCallIntent` objects to let you know when the user wants to place a video call using your app. A video call intent object contains the users to include in the call. It’s up to you to match the information in this object to contacts in your app and to initiate the resulting call.

Your Intents extension receives this intent when the user tries to initiate a call from the Siri interface. If your app supports CallKit, you may also receive this intent when the user tries to initiate a call from system interfaces such as the Recents tab of the Phone app.

To handle this intent, the handler object in your Intents extension must adopt the [`INStartVideoCallIntentHandling`](./instartvideocallintenthandling.md) protocol. Your handler confirms the request and creates an [`INStartVideoCallIntentResponse`](./instartvideocallintentresponse.md) object to indicate that it’s possible to begin the call. Don’t try to initiate calls directly from your Intents extension. SiriKit launches your app and passes it an [`NSUserActivity`](../Foundation/nsuseractivity.md) object that your app must then use to initiate the call. SiriKit places an [`INInteraction`](./ininteraction.md) object in the user activity object with this intent. For calls initiated through Siri, the interaction object also includes the response provided by your Intents extension.

For a list of other intents in the VoIP calling domain, see [`INCallsDomainHandling`](./incallsdomainhandling.md).

##### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri |
| Always requires unlocked device | If your app adopts CallKit, the system doesn’t require an unlocked device. Instead, your app runs in the background and the system displays the in-call user interface on your app’s behalf. ![](https://developer.apple.com/tutorials/images/com.apple.sirikit/spacer.png) If your app doesn’t adopt CallKit, SiriKit prompts the user to unlock the device so that it can launch your app. If the device is already unlocked, SiriKit launches the app in the foreground. |

Apps can optionally ask the user to unlock the device before handling this intent. To require unlocking of the device, include the name of this class in the `IntentsRestrictedWhileLocked` key of your Intents extension’s `Info.plist` file.

##### Example Phrases

There are many ways in which users can ask Siri to place a video call. The table below provides a few sample phrases in different languages. You can use these phrases during testing to trigger your intents. This list isn’t exhaustive and Siri may recognize many other phrases.

| Locale | Example 1 | Example 2 |
| --- | --- | --- |
| en |  |  |
| zh_CN |  |  |
| zh_HK | 喺`<appName>`打俾Gary |  |
| zh_TW | 用`<appName>`打視訊電話 |  |
| yue_CN | 喺打俾Gary |  |
| ar | مكالمة فيديو عبر `<appName>` | اتصل فيديو باستخدام `<appName>` |
| da |  |  |
| de | Videoanruf bei Hans mit `<appName>` | Videokonferenz mit Hans mit `<appName>` |
| es | Llamada de video a Salvador en `<appName>` | Vídeollamada a Gustavo por `<appName>` |
| fi | Soita videopuhelu Annalle `<appName>`illa | Soita `<appName>` kuvapuhelu Hannulle |
| fr | Fais un appel vidéo avec Alexandre sur `<appName>` | Appelle Alexandre sur `<appName>` avec la vidéo |
| he | תתקשרי למשה ב`<appName>` | תתקשרי ל-0525552222 באמצעות `<appName>` |
| it |  |  |
| ja | `<appName>`で山田にビデオ電話 | 山田に`<appName>`でビデオコール |
| ko | `<appName>`으로 충헌이한테 영상통화 해줘 | `<appName>`에서 충헌이한테 화상통화 해줘 |
| ms | Buat panggilan video `<appName>` | Buat panggilan video ke Aaron menggunakan `<appName>` |
| nb | Start en videosamtale til Stein med `<appName>` | Videosamtale med `<appName>` til Marie |
| nl | Start een videogesprek met Piet via `<appName>` | Bel Sara met video via `<appName>` |
| pt | Fazer uma ligação de vídeo pro João no `<appName>` | Ligar com vídeo para Maria usando `<appName>` |
| ru | Видео звонок моему папе по `<appName>` | Начать видео звонок с Ильёй через `<appName>` |
| sv | Ring ett videosamtal med `<appName>` till Erik | Ring Maja med `<appName>` videosamtal |
| th | Facetime หา ** ผ่าน `<appName>` |  |
| tr | Hasan’ı `<appName>` ile görüntülü ara | Halim’e `<appName>` üzerinden görüntülü arama yap |

In the preceding examples, `<appName>` represents the name of the app whose Intents extension initiates the call. If your app uses custom names for contacts, you can tell Siri about those names using the [`INVocabulary`](./invocabulary.md) class.

## Topics

### Initializing the Intent Object
- [init(contacts: [INPerson]?)](./instartvideocallintent/init%28contacts%29.md)
  Initializes the start video call intent object with the specified contacts.
### Getting the Recipients of the Call
- [var contacts: [INPerson]?](./instartvideocallintent/contacts.md)
  The users to call.

## Relationships

### Inherits From
- [INIntent](./inintent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [INIntentSetImageKeyPath](./inintentsetimagekeypath.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Video Call Initiation
- [protocol INStartVideoCallIntentHandling](./instartvideocallintenthandling.md)
  The handler interface for initiating a video call from your app.
- [class INStartVideoCallIntentResponse](./instartvideocallintentresponse.md)
  A response to an intent to start a video call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartvideocallintent)*