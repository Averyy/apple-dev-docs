# INSetCarLockStatusIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to lock or unlock the user’s car.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INSetCarLockStatusIntent
```

```objc
@interface INSetCarLockStatusIntent : INIntent
```

## Overview

When the user asks to lock or unlock the car, Siri creates an `INSetCarLockStatusIntent` object. This intent object can contain the name of the user’s car and the requested lock status. Use this object to lock or unlock the car.

To handle this intent, the handler object in your Intents extension must adopt the [`INSetCarLockStatusIntentHandling`](./insetcarlockstatusintenthandling.md) protocol. Your handler should confirm the request and create an [`INSetCarLockStatusIntentResponse`](./insetcarlockstatusintentresponse.md) object with the results.

### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents, Siri Suggestions |
| Always requires unlocked device? | Yes |

### Example Phrases

Users can ask Siri to lock or unlock their car in a variety of ways. The table below provides a few sample phrases in different languages. You can use these phrases during testing to trigger your intents. This list isn’t exhaustive, and Siri may recognize many other phrases.

| Locale | Example 1 | Example 2 |
| --- | --- | --- |
| en | Lock my car. | Unlock my truck. |
| zh_CN | 把车锁上。 | 给后备箱解锁。 |
| zh_HK | 幫我鎖車 | 幫手開部卡車嘅鎖 |
| zh_TW | 鎖上車子。 | 解鎖卡車。 |
| yue_CN | 帮我锁车 | 帮手开部卡车嘅锁 |
| ar | اقفل سيارتي | افتح قفل شاحنتي |
| da | Lås min bil | Lås min bil op |
| de | Schließe mein Auto ab | Schließe mein Auto auf |
| es | Cierra el coche. | Abre la camioneta. |
| fi | Lukitse auto | Avaa auto |
| fr | Ferme ma voiture. | Ouvre ma voiture. |
| he | תנעלי את הרכב שלי | פתח את הרכב שלי |
| it | Chiudi la mia auto. | Apri la mia auto. |
| ja | 車をロックして | トラックのロックを解除して |
| ko | 차 잠가줘 | 트럭 열어줘 |
| ms | Kunci kereta saya | Buka kunci trak saya |
| nb | Lås bilen min | Lås opp bilen min |
| nl | Doe mijn auto op slot. | Open mijn auto. |
| pt | Tranca meu carro | Destrancar meu carro |
| ru | Закрой мою машину. | Открой мой грузовик |
| sv | Lås min bil. | Lås upp min lastbil. |
| th | ล็อครถ | ปลดล็อครถ |
| tr | Arabamı kilitle. | Aracımın kilidini aç. |

Unlike other SiriKit intents, these phrases do not always require your app’s name. Siri infers the app name when possible (for example, based on unique user vocabulary registered by your app). If necessary, Siri verifies the app’s name before launching your extension.

## Topics

### Initializing the Intent Object
- [convenience init(locked: Bool?, carName: INSpeakableString?)](./insetcarlockstatusintent/init%28locked,carname%29.md)
  Initializes an intent to set the lock status of the named car.
- [- initWithLocked:carName:](./insetcarlockstatusintent/initwithlocked_carname_.md)
  Initializes an intent to set the lock status of the named car.
### Getting the Car Name
- [var carName: INSpeakableString?](./insetcarlockstatusintent/carname.md)
  A name that identifies the user’s car.
### Getting the Locked Status
- [var locked: Bool?](./insetcarlockstatusintent/locked-9h0kx.md)
  A Boolean value that indicates whether to lock the car.
- [locked](./insetcarlockstatusintent/locked-61uw4.md)
  A Boolean value that indicates whether to lock the car.

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

### Set Car Lock Status
- [protocol INSetCarLockStatusIntentHandling](./insetcarlockstatusintenthandling.md)
  The handler interface for requesting to lock or unlock a car.
- [class INSetCarLockStatusIntentResponse](./insetcarlockstatusintentresponse.md)
  Your app’s response to a request to lock or unlock the car.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetcarlockstatusintent)*