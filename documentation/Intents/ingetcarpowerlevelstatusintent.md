# INGetCarPowerLevelStatusIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request for the current power level of the user’s car.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INGetCarPowerLevelStatusIntent
```

```objc
@interface INGetCarPowerLevelStatusIntent : INIntent
```

#### Overview

When asked for the car’s power level, Siri creates an `INGetCarPowerLevelStatusIntent` object. This intent object can contain the name of the user’s car. Use this object to provide information about the car’s current power level.

To handle this intent, the handler object in your Intents extension must adopt the [`INGetCarPowerLevelStatusIntentHandling`](./ingetcarpowerlevelstatusintenthandling.md) protocol. Your handler should confirm the request and create an [`INGetCarPowerLevelStatusIntentResponse`](./ingetcarpowerlevelstatusintentresponse.md) object with the results.

##### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents, Siri Suggestions |
| Always requires unlocked device? | Yes |

##### Example Phrases

Users can ask Siri for their car’s power level in a variety of ways. The table below provides a few sample phrases in different languages. You can use these phrases during testing to trigger your intents. This list isn’t exhaustive, and Siri may recognize many other phrases.

| Locale | Example 1 | Example 2 |
| --- | --- | --- |
| en | How much gas is left in my car? | How far can I drive my car on the current charge? |
| zh_CN | 我的车还剩多少油？ | 当前电量够我开多远？ |
| zh_HK | 部車仲有幾多油 | 以而家嘅油量，我架車仲可以行幾遠？ |
| zh_TW | 車子還剩多少油？ | 車子電量還可以開多久？ |
| yue_CN | 部车仲有几多油 | 我架车剩低嘅油仲可以行几远？ |
| ar | كم تبقى من الوقود في سيارتي؟ | إلى أي مدى يمكن أن أقود سيارتي على الطاقة الحالية؟ |
| da | Hvor meget benzin er der tilbage i min bil | Hvor langt kan jeg køre på denne opladning |
| de | Wie viel Benzin habe ich noch? | Wie weit komme ich noch mit der Batterieladung meines Autos? |
| es | ¿Cuánta gasolina me queda en el coche? | ¿Cuánta carga tiene el auto? |
| fi | Miten paljon autossa on bensaa jäljellä | Miten pitkälle autolla pääsee nykyisellä latauksella |
| fr | combien me reste-t-il d’essence dans ma voiture ? | combien de kilomètres je peux encore parcourir |
| he | כמה דלק נשאר לי באוטו | כמה רחוק אני יכולה לנסוע עם מצב הצמיגים הנוכחי |
| it | Quanta benzina ho nella mia auto? | Quanti chilometri posso percorrere con la mia auto? |
| ja | この車のガソリンはどれくらい残っている? | 今の充電量でこの車はあとどれくらい走れる? |
| ko | 기름 얼마나 남았어? | 현재 충전량으로 얼마나 운전할 수 있어? |
| ms | Apakah baki petrol dalam kereta saya? | Berapa jauh boleh saya pandu kereta saya pada cas semasa? |
| nb | Hvor mye bensin er det igjen på bilen min? | Hvor langt kan jeg kjøre med nåværende ladning? |
| nl | Hoeveel benzine is er nog in de auto? | Hoe ver kan mijn auto nog rijden? |
| pt | Quanto de combustível meu carro ainda tem? | Quantos quilômetros posso dirigir com a carga atual? |
| ru | Сколько бензина осталось в моей машине? | Как далеко я могу проехать на текущей зарядке? |
| sv | Hur mycket bensin finns det kvar i bilen? | Hur långt kan jag köra på den nuvarande laddningen? |
| th | รถเหลือน้ำมันเท่าไหร่ | รถเหลือพลังงานแบตเตอรี่ไปได้อีกไกลเท่าไหร่ |
| tr | Arabada ne kadar benzin kaldı? | Arabada kalan şarjla ne kadar yol gidebilirim? |

Users are likely to ask for specific types of data (fuel, charge, or distance), but the intent doesn’t distinguish between these requests. Always return all the data you can from the car. For example, return the percentage of fuel remaining for a fuel-driven car, the percentage of charge remaining for an electric car, and (wherever possible) an estimated distance remaining.

Unlike other SiriKit intents, these phrases do not always require your app’s name. Siri infers the app name when possible (for example, based on unique user vocabulary registered by your app). If necessary, Siri verifies the app’s name before launching your extension.

## Topics

### Initialzing the Intent Object
- [init(carName: INSpeakableString?)](./ingetcarpowerlevelstatusintent/init%28carname%29.md)
  Initializes a car power intent with the provided car name.
### Getting the Car Name
- [var carName: INSpeakableString?](./ingetcarpowerlevelstatusintent/carname.md)
  A name that identifies the user’s car.

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

### Get Car Power Level Status
- [protocol INGetCarPowerLevelStatusIntentHandling](./ingetcarpowerlevelstatusintenthandling.md)
  The handler interface for requesting a car’s current power level.
- [class INGetCarPowerLevelStatusIntentResponse](./ingetcarpowerlevelstatusintentresponse.md)
  Your app’s response to a request for the vehicle power level.
- [protocol INGetCarPowerLevelStatusIntentResponseObserver](./ingetcarpowerlevelstatusintentresponseobserver.md)
  The interface for providing updates of a vehicle’s power level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintent)*