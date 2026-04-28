# EnergySaver.Com.apple.EnergySaver.desktop.Schedule.RepeatingPowerOff

**Framework**: Device Management  
**Kind**: dictionary

The triggers for turning the device off.

**Availability**:
- macOS 10.7+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object EnergySaver.Com.apple.EnergySaver.desktop.Schedule.RepeatingPowerOff
```

## Properties

- `eventtype` (string) *(required)*: The type of action defined by this schedule.
- `time` (integer): The time, in minutes, since midnight.
- `weekdays` (integer): One or more days of the week in an unsigned integer bitmap: - `1` = Mon
- `2` = Tue
- `4` = Wed
- `8` = Thu
- `16` = Fri
- `32` = Sat
- `64` = Sun

## See Also

- [object EnergySaver.Com.apple.EnergySaver.desktop.Schedule.RepeatingPowerOn](energysaver/com.apple.energysaver.desktop.schedule-data.dictionary/repeatingpoweron-data.dictionary.md)
  The triggers for turning the device on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/energysaver/com.apple.energysaver.desktop.schedule-data.dictionary/repeatingpoweroff-data.dictionary)*