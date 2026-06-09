# EnergySaver.Com.apple.EnergySaver.desktop.Schedule.RepeatingPowerOn

**Framework**: Device Management  
**Kind**: dictionary

The triggers for turning the device on.

**Availability**:
- macOS 10.7+

## Declaration

```swift
object EnergySaver.Com.apple.EnergySaver.desktop.Schedule.RepeatingPowerOn
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

- [object EnergySaver.Com.apple.EnergySaver.desktop.Schedule.RepeatingPowerOff](energysaver/com.apple.energysaver.desktop.schedule-data.dictionary/repeatingpoweroff-data.dictionary.md)
  The triggers for turning the device off.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/energysaver/com.apple.energysaver.desktop.schedule-data.dictionary/repeatingpoweron-data.dictionary)*