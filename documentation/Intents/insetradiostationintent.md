# INSetRadioStationIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to change the current radio station.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INSetRadioStationIntent
```

```objc
@interface INSetRadioStationIntent : INIntent
```

#### Overview

When the user asks Siri to change the current radio station, SiriKit creates an [`INSetRadioStationIntent`](./insetradiostationintent.md) object and delivers it to the app’s Intents extension. You use the intent to identify which radio station the user wants. Automotive vendors can use this intent to change the settings on a vehicle’s built-in entertainment system.

This properties of this class support identifying a radio station in several different ways, but a given instance of this class contains doesn’t populate all of those properties. When resolving and confirming the parameters of this intent, use the properties that are available to change the station.

The object that handles this intent must adopt the [`INSetRadioStationIntentHandling`](./insetradiostationintenthandling.md) protocol. Use this intent object to identify the selected station and to create an [`INSetRadioStationIntentResponse`](./insetradiostationintentresponse.md) object indicating the results of changing the station.

##### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents |
| Always requires unlocked device | Yes |

##### Example Phrases

There are many ways in which users can ask Siri to change the radio station. The table below provides a few sample phrases in different languages. You can use these phrases during testing to trigger your intents. This list isn’t exhaustive and Siri may recognize many other phrases.

| Locale | Example 1 | Example 2 |
| --- | --- | --- |
| en | Tune into 88.5 FM | Switch to FM radio preset 3 |
| zh_CN | 转到FM88.5 | 转到预设的FM三台 |
| zh_HK | 校去FM88.5 | 轉去FM收音機三號台 |
| zh_TW | 轉到FM88.5 | 換到FM收音機三號預設台 |
| yue_CN | 轉到FM88.5 | 转去FM收音机三号台 |
| ar |  |  |
| da | Stil ind på 88,5 FM | Skift til FM Radio 3 |
| de | Stelle Radio auf 88.5 FM | Wechsele zu Radiostation 3 |
| es | Sintoniza 88.5 FM | Escuchar radio FM |
| fi | Viritä radio taajuudelle 88.5 MHz | Laita radio esivalinnalle 3 |
| fr | Mets la radio sur 88.5 FM | Mets la radio sur 3 |
| he |  |  |
| it | Sintonizza 88.5 FM | Metti la radio FM al preset tre |
| ja | 88.5FMに合わせて | FMラジオのプリセット3をかけて |
| ko | FM 88.5 켜줘 | FM 라디오 프리셋 3으로 변경해줘 |
| ms | Dengarkan frekuensi 88.5 FM | Tukar ke pratetap radio 3 |
| nb | Still inn 88,5 FM | Bytt til kanal 3 |
| nl | Stem af op 88.5 FM | Verander naar FM radio voorkeuze 3 |
| pt | Sintonizar na 88.5 FM | Trocar para rádio FM número 3 |
| ru | Включи 88.5 FM | Включи радио на настройку 3 |
| sv | Skruva in 88,5 FM | Ändra FM radion till kanal 3 |
| th | เปลี่ยนเป็น FM 88.5 | เปลี่ยนไปที่ช่องวิทยุเบอร์ 3 |
| tr | 88.5 FM’i aç | 3 numarada kayıtlı radyoya geç |

When managing CarPlay features, users don’t need to include the name of the app in the phrases that they speak. Siri knows automatically when CarPlay is active and routes CarPlay-related intents to the app of the corresponding automotive vendor.

## Topics

### Initializing the Intent Object
- [convenience init(radioType: INRadioType, frequency: Double?, stationName: String?, channel: String?, presetNumber: Int?)](./insetradiostationintent/init%28radiotype,frequency,stationname,channel,presetnumber%29.md)
  Initializes the intent object with the specified climate settings information.
- [- initWithRadioType:frequency:stationName:channel:presetNumber:](./insetradiostationintent/initwithradiotype_frequency_stationname_channel_presetnumber_.md)
  Initializes the intent object with the specified climate settings information.
### Getting Details About the Radio Station to Set
- [var radioType: INRadioType](./insetradiostationintent/radiotype.md)
  The type of radio tuner to use.
- [var frequency: Double?](./insetradiostationintent/frequency-2ctw6.md)
  The broadcast frequency of the radio station.
- [var stationName: String?](./insetradiostationintent/stationname.md)
  The name associated with the radio station.
- [var channel: String?](./insetradiostationintent/channel.md)
  The channel number of the station.
- [var presetNumber: Int?](./insetradiostationintent/presetnumber-2dub4.md)
  The programmable preset assigned to the station.
- [frequency](./insetradiostationintent/frequency-63rbb.md)
  The broadcast frequency of the radio station.
- [presetNumber](./insetradiostationintent/presetnumber-20pv7.md)
  The programmable preset assigned to the station.

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

### CarPlay Radio Station Settings
- [protocol INSetRadioStationIntentHandling](./insetradiostationintenthandling.md)
  The handler interface for changing a radio station.
- [class INSetRadioStationIntentResponse](./insetradiostationintentresponse.md)
  Your app’s response to a set radio station intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetradiostationintent)*