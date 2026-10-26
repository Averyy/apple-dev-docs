# INStartAudioCallIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to start an audio-only call with one or more users.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 6.0

> **Deprecated**: Use [`INStartCallIntent`](./instartcallintent.md) instead.

## Declaration

```swift
class INStartAudioCallIntent
```

```objc
@interface INStartAudioCallIntent : INIntent
```

#### Overview

SiriKit creates [`INStartAudioCallIntent`](./instartaudiocallintent.md) objects when the user wants to place an audio call using your app. An audio call intent object contains the users to call. Your intent handler matches the information in this object to contacts in your app and to initiate the resulting call.

Your Intents extension receives this intent when the user tries to initiate a call from the Siri interface. If your app supports CallKit, you may also receive this intent when the user tries to initiate a call from system interfaces such as the Recents tab of the Phone app.

To handle this intent, the handler object in your Intents extension must adopt the [`INStartAudioCallIntentHandling`](./instartaudiocallintenthandling.md) protocol. Use your handler to confirm the request and create an [`INStartAudioCallIntentResponse`](./instartaudiocallintentresponse.md) object to indicate that it’s possible to begin the call. Don’t try to initiate calls directly from your Intents extension. SiriKit launches your app and passes it an [`NSUserActivity`](../Foundation/nsuseractivity.md) object that your app must then use to initiate the call. SiriKit places an [`INInteraction`](./ininteraction.md) object in the user activity object with this intent. For calls initiated through Siri, the interaction object also includes the response provided by your Intents extension.

For a list of other intents in the VoIP calling domain, see [`INCallsDomainHandling`](./incallsdomainhandling.md).

##### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri |
| Always requires unlocked device | If your app adopts CallKit, the system doesn’t require an unlocked device. Instead, your app runs in the background and the system displays the in-call user interface on your app’s behalf. ![](https://developer.apple.com/tutorials/images/com.apple.sirikit/spacer.png) If your app doesn’t adopt CallKit, SiriKit prompts the user to unlock the device so that it can launch your app. If the device is already unlocked, SiriKit launches the app in the foreground. |

Apps can optionally ask the user to unlock the device before handling this intent. To require unlocking of the device, include the name of this class in the `IntentsRestrictedWhileLocked` key of your Intents extension’s `Info.plist` file.

##### Example Phrases

Users can ask Siri to place an audio call. The table below provides a few sample phrases in different languages. You can use these phrases during testing to trigger your intents. This list isn’t exhaustive and Siri may recognize many other phrases.

| Locale | Example 1 | Example 2 |
| --- | --- | --- |
| en | Call Andrew on `<appName>` |  |
| zh_CN | 用`<appName>`打电话给13800123455 |  |
| zh_HK | 喺`<appName>`打電話比小明 | 喺`<appName>`打電話比Jeffrey |
| zh_TW | 用`<appName>`打電話 |  |
| yue_CN | 喺打电话比小明 | 喺打电话比Jeffrey |
| ar | اتصل ب رنا عبر `<appName>` | اتصال على محمد عن طريق `<appName>` |
| da | Ring til Peter med `<appName>` | via fyi lav et opkald til john |
| de | Ruf Thomas mit `<appName>` an | Rufe Thomas an mit `<appName>` |
| es | Llámale a Sandra por `<appName>` | Llamar a Juan con `<appName>` |
| fi | Soita `<appName>`lla Antille | Pirauta Annalle `<appName>`lla |
| fr | Contacte Jean avec `<appName>` | Appelle Halim sur `<appName>` |
| he | תתקשרי למשה ב`<appName>` | תתקשרי למשה באמצעות `<appName>` |
| it | Chiama Riccardo usando `<appName>` |  |
| ja | `<appName>`で花子に電話 | 花子に`<appName>`で電話 |
| ko | `<appName>`을 사용해서 충헌이한테 전화해 | `<appName>`로 충헌한테 전화해 |
| ms | Telefon Alham menggunakan `<appName>` | Buat panggilan `<appName>` ke Sherly |
| nb | Ring Petter med `<appName>` | Ring med `<appName>` til Stian |
| nl | Bel Jan via `<appName>` | Telefoneer naar Marie met `<appName>` |
| pt | Ligar pro Rafael utilizando `<appName>` | Liga para Maria no `<appName>` |
| ru | Позвони Илье с помощью `<appName>` | А ты можешь позвонить Анне по `<appName>` |
| sv | Använd `<appName>` och ring upp Johan | Ring ett `<appName>` samtal till Lisen |
| th | โทรหาวิภาวีโดยใช้ `<appName>` |  |
| tr | Hasan’ı `<appName>` ile ara | Halim’i `<appName>` üzerinden ara |

In the preceding examples, `<appName>` represents the name of the app whose Intents extension initiates the call. If your app uses custom names for contacts, you can tell Siri about those names using the [`INVocabulary`](./invocabulary.md) class.

## Topics

### Creating the Intent Object
- [init(destinationType: INCallDestinationType, contacts: [INPerson]?)](./instartaudiocallintent/init%28destinationtype,contacts%29.md)
  Creates an intent with the specified information.
- [convenience init(contacts: [INPerson]?)](./instartaudiocallintent/init%28contacts%29.md)
  Initializes the start audio call intent object with the specified contacts.
### Getting the Call Attributes
- [var contacts: [INPerson]?](./instartaudiocallintent/contacts.md)
  The users to call.
- [var destinationType: INCallDestinationType](./instartaudiocallintent/destinationtype.md)
  The type of call to place.

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

### Audio Call Initiation
- [protocol INStartAudioCallIntentHandling](./instartaudiocallintenthandling.md)
  The handler interface for initiating an audio call from your app.
- [class INStartAudioCallIntentResponse](./instartaudiocallintentresponse.md)
  An app’s response to an intent to start an audio call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartaudiocallintent)*