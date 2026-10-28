# INSetClimateSettingsInCarIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to change the climate settings in a CarPlay-enabled vehicle.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INSetClimateSettingsInCarIntent
```

```objc
@interface INSetClimateSettingsInCarIntent : INIntent
```

## Overview

Automotive vendors can add support for this intent to an Intents extension that they ship with their automotive apps. When the user asks Siri to change a setting related to the vehicle’s climate control, Siri creates an [`INSetClimateSettingsInCarIntent`](./insetclimatesettingsincarintent.md) object and delivers it to the app’s Intents extension. You use the intent to identify which setting the user wants to change.

This class contains properties for multiple types of climate settings, but a given instance of this class contains changes for only one system at a time. When resolving and confirming the parameters of this intent, use the specified properties to modify your vehicle’s settings. Assume no changes for other settings. If your vehicle doesn’t support a particular setting, offer a reasonable fallback setting and ask the user for confirmation.

The object that handles this intent must adopt the [`INSetClimateSettingsInCarIntentHandling`](./insetclimatesettingsincarintenthandling.md) protocol. Use this intent object to identify which setting changed and to create an [`INSetClimateSettingsInCarIntentResponse`](./insetclimatesettingsincarintentresponse.md) object indicating the results of changing the climate settings.

### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents (in conjunction with CarPlay) |
| Always requires unlocked device | Yes |

### Example Phrases

Users can ask Siri to change the climate settings in a vehicle in a variety of ways. The table below provides a few sample phrases in different languages. You can use these phrases during testing to trigger your intents. This list isn’t exhaustive and Siri may recognize many other phrases.

| Locale | Example 1 | Example 2 |
| --- | --- | --- |
| en | Turn on the AC | Turn the fan to max |
| zh_CN | 打开空调 | 空调调到最高 |
| zh_HK | 打開空調 | 空調較到最大 |
| zh_TW | 打開空調 | 空調調到最強 |
| yue_CN | 打开空调 | 空调较到最大 |
| ar | شغل تكييف الهواء | أطفأ التحكم بالمناخ |
| da | tænd for klimaanlægget | Skru blæseren op på max |
| de | Klimaanlage einschalten | Schalte Klimaanlage ein |
| es | Prende el aire acondicionado | Pon el climatizador a 20 grados |
| fi | Laita ilmastointi päälle | Laita tuuletin täysille |
| fr | Allume le chauffage | Branche le chauffage |
| he | תרימי את הבקרת אקלים |  |
| it | Accendi l’aria condizionata | Metti la ventola al massimo |
| ja | エアコンをオンにして | ファンを最大にして |
| ko | 에어콘 켜줘 | 팬을 최대로 틀어줘 |
| ms | Hidupkan pendingin hawa | Setkan kipas ke posisi maksimum |
| nb | Skru på klimaanlegget | Skru viften opp til maks |
| nl | Zet de airconditioning aan | Zet de ventilator op het maximum |
| pt | Ligar o ar condicionado | Coloque o ventilador no máximo |
| ru | Включи кондиционер | Сделай обдув на максимум |
| sv | ändra klimatkontrollen till auto | byt klimat till automatiskt |
| th | เปิดแอร์ | เปิดพัดลมระดับสูงสุด |
| tr | Klimayı aç | Fanı sonuna kadar aç |

When managing CarPlay features, users don’t need to include the name of the app in the phrases that they speak. Siri knows automatically when CarPlay is active and routes CarPlay-related intents to the app of the corresponding automotive vendor.

## Topics

### Initializing the Intent Object
- [convenience init(enableFan: Bool?, enableAirConditioner: Bool?, enableClimateControl: Bool?, enableAutoMode: Bool?, airCirculationMode: INCarAirCirculationMode, fanSpeedIndex: Int?, fanSpeedPercentage: Double?, relativeFanSpeedSetting: INRelativeSetting, temperature: Measurement<UnitTemperature>?, relativeTemperatureSetting: INRelativeSetting, climateZone: INCarSeat, carName: INSpeakableString?)](./insetclimatesettingsincarintent/init%28enablefan,enableairconditioner,enableclimatecontrol,enableautomode,aircirculationmode,fanspeedindex,fanspeedpercentage,relativefanspeedsetting,temperature,relativetemperaturesetting,climatezone,carname%29.md)
  Creates the intent object with the specified climate settings information.
- [- initWithEnableFan:enableAirConditioner:enableClimateControl:enableAutoMode:airCirculationMode:fanSpeedIndex:fanSpeedPercentage:relativeFanSpeedSetting:temperature:relativeTemperatureSetting:climateZone:carName:](./insetclimatesettingsincarintent/initwithenablefan_enableairconditioner_enableclimatecontrol_enableautomode_aircirculationmode_fanspeedindex_fanspeedpercentage_relativefanspeedsetting_temperature_relativetemperaturesetting_climatezone_carname_.md)
  Initializes the intent object with the specified climate settings information.
- [- initWithEnableFan:enableAirConditioner:enableClimateControl:enableAutoMode:airCirculationMode:fanSpeedIndex:fanSpeedPercentage:relativeFanSpeedSetting:temperature:relativeTemperatureSetting:climateZone:](./insetclimatesettingsincarintent/initwithenablefan_enableairconditioner_enableclimatecontrol_enableautomode_aircirculationmode_fanspeedindex_fanspeedpercentage_relativefanspeedsetting_temperature_relativetemperaturesetting_climatezone_.md)
  Initializes the intent object with the specified climate settings information.
### Getting the Car Name
- [var carName: INSpeakableString?](./insetclimatesettingsincarintent/carname.md)
  A name that identifies the user’s car.
### Getting the Climate Control Settings
- [var enableClimateControl: Bool?](./insetclimatesettingsincarintent/enableclimatecontrol-4y9iz.md)
  A Boolean value indicating whether to turn on the climate control system.
- [var enableAutoMode: Bool?](./insetclimatesettingsincarintent/enableautomode-31bzq.md)
  A Boolean value indicating whether to enable automatic mode for the climate control system.
- [var airCirculationMode: INCarAirCirculationMode](./insetclimatesettingsincarintent/aircirculationmode.md)
  The air circulation mode for the climate control system.
- [var temperature: Measurement<UnitTemperature>?](./insetclimatesettingsincarintent/temperature.md)
  The specific temperature to set for the climate control system.
- [var relativeTemperatureSetting: INRelativeSetting](./insetclimatesettingsincarintent/relativetemperaturesetting.md)
  A relative temperature setting.
- [var climateZone: INCarSeat](./insetclimatesettingsincarintent/climatezone.md)
  The seat position to have its climate settings modified.
- [enableClimateControl](./insetclimatesettingsincarintent/enableclimatecontrol-tviy.md)
  A Boolean value indicating whether to turn on the climate control system.
- [enableAutoMode](./insetclimatesettingsincarintent/enableautomode-6ye2n.md)
  A Boolean value indicating whether to enable automatic mode for the climate control system.
### Getting the Fan Settings
- [var enableFan: Bool?](./insetclimatesettingsincarintent/enablefan-5srs9.md)
  A Boolean value indicating whether to turn on the cabin fan system.
- [var fanSpeedIndex: Int?](./insetclimatesettingsincarintent/fanspeedindex-wz49.md)
  An integer value indicating the desired fan speed position.
- [var fanSpeedPercentage: Double?](./insetclimatesettingsincarintent/fanspeedpercentage-7i2hq.md)
  A floating-point value indicating the requested fan speed specified as a percentage of the maximum speed.
- [var relativeFanSpeedSetting: INRelativeSetting](./insetclimatesettingsincarintent/relativefanspeedsetting.md)
  A relative fan speed setting.
- [enableFan](./insetclimatesettingsincarintent/enablefan-3bu9e.md)
  A Boolean value indicating whether to turn on the cabin fan system.
- [fanSpeedIndex](./insetclimatesettingsincarintent/fanspeedindex-4c1rr.md)
  An integer value indicating the desired fan speed position.
- [fanSpeedPercentage](./insetclimatesettingsincarintent/fanspeedpercentage-ep0u.md)
  A floating-point value indicating the requested fan speed specified as a percentage of the maximum speed.
### Getting the Air Conditioner Settings
- [var enableAirConditioner: Bool?](./insetclimatesettingsincarintent/enableairconditioner-9q3dr.md)
  A Boolean value indicating whether to turn on the air conditioner system.
- [enableAirConditioner](./insetclimatesettingsincarintent/enableairconditioner-3prnk.md)
  A Boolean value indicating whether to turn on the air conditioner system.

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

### CarPlay Climate Settings
- [protocol INSetClimateSettingsInCarIntentHandling](./insetclimatesettingsincarintenthandling.md)
  The handler interface for changing a vehicle’s climate control settings.
- [class INSetClimateSettingsInCarIntentResponse](./insetclimatesettingsincarintentresponse.md)
  Your app’s response to a set climate settings in car intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetclimatesettingsincarintent)*