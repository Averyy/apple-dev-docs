# INSetMessageAttributeIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to modify the attributes of a message.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class INSetMessageAttributeIntent
```

```objc
@interface INSetMessageAttributeIntent : INIntent
```

#### Overview

Siri creates an [`INSetMessageAttributeIntent`](./insetmessageattributeintent.md) object when the user asks to modify the attributes of one or more messages. Attributes represent information about the message such as whether the user read or flagged the message. This intent object includes the messages to modify and which attributes to change.

To handle this intent, the handler object in your Intents extension must adopt the [`INSetMessageAttributeIntentHandling`](./insetmessageattributeintenthandling.md) protocol. Your handler should confirm the request and create an [`INSetMessageAttributeIntentResponse`](./insetmessageattributeintentresponse.md) object with the results of modifying the messages.

##### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents |
| Always requires unlocked device | No |

Apps can optionally ask the user to unlock the device before handling this intent. To require unlocking of the device, include the name of this class in the `IntentsRestrictedWhileLocked` key of your Intents extension’s `Info.plist` file.

##### Example Phrases

Users can ask Siri to set the attributes of a message in a variety of ways. The table below provides a few sample phrases in different languages. You can use these phrases during testing to trigger your intents. This list is not exhaustive and Siri may recognize many other phrases.

| Locale | Example 1 | Example 2 |
| --- | --- | --- |
| en | Read my messages from Bob using `<appName>` |  |
| zh_CN | 读一下来自李宏辉的`<appName>`信息 | 读一下`<appName>`上李宏辉的信息 |
| zh_HK | 用`<appName>`讀Jeffrey俾我嘅訊息 | 讀出`<appName>`上邊嘅訊息 |
| zh_TW | 朗讀我`<appName>`的訊息 | 在`<appName>`上朗讀我的訊息 |
| yue_CN | 用`<appName>`读Jeffrey俾我嘅讯息 | 朗读`<appName>`嘅信息 |
| ar | إقرأ رسائل `<appName>` من عامر | قراءة آخر رسالة `<appName>` لرنا |
| da | læs mine nye `<appName>` beskeder | læs mine nye `<appName>` beskeder |
| de | Die `<appName>` Nachricht vorlesen | Lies meine `<appName>` Nachricht vor |
| es | Leer los mensajes de Sandra usando `<appName>` | Léeme los mensajes que me mandó Pedro por `<appName>` |
| fi | Lue mun `<appName>` viestit Paavolta | Lue Julialta tulleet `<appName>` viestit |
| fr | Lis mes messages de Jean sur `<appName>` | Lis mes messages écrits par Henri sur `<appName>` |
| he | תקרא את ההודעות מדויד באמצעות `<appName>` | באמצעות `<appName>` תקרא את ההודעות מדויד |
| it | Leggi i miei messaggi da Rosanna su `<appName>` | Leggi i miei messaggi su `<appName>` |
| ja | `<appName>`で太郞からのメッセージを読んで | 太郞からの`<appName>`メッセージを読み上げて |
| ko | 내 새로운 `<appName>` 메시지를 읽어줘 | 나의 `<appName>` 메시지 읽어줘 |
| ms | Baca mesej `<appName>` saya | Baca teks dari Dini dalam `<appName>` |
| nb | Les mine nye `<appName>` meldinger | Les meldingen i `<appName>` |
| nl | Lees mijn nieuwe `<appName>` berichten | Lees mijn nieuwe `<appName>` berichten |
| pt | Leia minha mensagem do João no `<appName>` | Leia a última mensagem recebida no `<appName>` |
| ru | Прочти мои новые `<appName>` сообщения | Прочитай новые сообщения в`<appName>` |
| sv | Läs mina nya `<appName>` meddelanden | Läs upp nya meddelanden på `<appName>` |
| th | อ่านข้อความจาก `<appName>` ของสมชาย | อ่านข้อความของสมชายที่ส่งมาจาก `<appName>` |
| tr | `<appName>`’den gelen mesajı oku | `<appName>` uygulamasındaki mesajı oku |

In the preceding examples, `<appName>` represents the name of the app whose Intents extension modifies the message attributes.

## Topics

### Initializing the Intent Object
- [init(identifiers: [String]?, attribute: INMessageAttribute)](./insetmessageattributeintent/init%28identifiers,attribute%29.md)
  Initializes the set message attribute intent object with the specified identifiers and attribute.
### Getting the Attribute Details
- [var attribute: INMessageAttribute](./insetmessageattributeintent/attribute.md)
  The attribute to apply to the messages.
- [var identifiers: [String]?](./insetmessageattributeintent/identifiers.md)
  The array of message identifiers.

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

### Setting Message Attributes
- [protocol INSetMessageAttributeIntentHandling](./insetmessageattributeintenthandling.md)
  An interface that handles modifying message attributes.
- [class INSetMessageAttributeIntentResponse](./insetmessageattributeintentresponse.md)
  Your app’s response to a set message attribute intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetmessageattributeintent)*