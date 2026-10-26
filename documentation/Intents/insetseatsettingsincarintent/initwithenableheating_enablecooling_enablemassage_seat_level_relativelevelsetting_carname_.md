# initWithEnableHeating:enableCooling:enableMassage:seat:level:relativeLevelSetting:carName:

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Initializes the intent object with the specified climate settings information.

**Availability**:
- iOS 12.0+ - Deprecated in 15.0
- iPadOS 12.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```objc
- (instancetype) initWithEnableHeating:(NSNumber *) enableHeating enableCooling:(NSNumber *) enableCooling enableMassage:(NSNumber *) enableMassage seat:(INCarSeat) seat level:(NSNumber *) level relativeLevelSetting:(INRelativeSetting) relativeLevelSetting carName:(INSpeakableString *) carName;
```

#### Return Value

An initialized intent object or `nil` if the object could not be created.

#### Discussion

Normally, you do not create instances of this class yourself. Instead, Siri creates instances when the user asks to change the vehicle’s seat settings. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths. Your test code should modify the settings for only one system at a time.

## Parameters

- `enableHeating`: A Boolean value indicating whether to enable the seat heater system. Specify `nil` if you don’t want to modify this setting.
- `enableCooling`: A Boolean value indicating whether to enable the seat cooling system. Specify `nil` if you don’t want to modify this setting.
- `enableMassage`: A Boolean value indicating whether to enable the seat massage system. Specify `nil` if you don’t want to modify this setting.
- `seat`: The seat position to modify.
- `level`: The heating, cooling, or massage level, specified as an integer indicating the position of the corresponding controls. Specify `nil` if you don’t want to use this parameter to make the change.
- `relativeLevelSetting`: The heating, cooling, or massage level, specified as a change relative to the current level. Specify `nil` if you don’t want to use this parameter to make the change.
- `carName`: The name of the car to apply the settings to.

## See Also

### Initializing the Intent Object
- [- initWithEnableHeating:enableCooling:enableMassage:seat:level:relativeLevelSetting:](./initwithenableheating_enablecooling_enablemassage_seat_level_relativelevelsetting_.md)
  Initializes the intent object with the specified climate settings information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetseatsettingsincarintent/initwithenableheating:enablecooling:enablemassage:seat:level:relativelevelsetting:carname:)*