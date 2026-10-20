# EnergySaver.Com.apple.EnergySaver.desktop.Schedule.RepeatingPowerOff

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

The triggers for turning the device off.

**Availability**:
- macOS 10.7+

## Declaration

```
object EnergySaver.Com.apple.EnergySaver.desktop.Schedule.RepeatingPowerOff
```

## Properties

- `eventtype` (string) *(required)*: The type of action defined by this schedule.

  **Allowed Values**: `wake`, `poweron`, `wakepoweron`, `sleep`, `shutdown`, `restart`
- `time` (integer): The time, in minutes, since midnight.
- `weekdays` (integer): One or more days of the week in an unsigned integer bitmap:

  - `1` = Mon
  - `2` = Tue
  - `4` = Wed
  - `8` = Thu
  - `16` = Fri
  - `32` = Sat
  - `64` = Sun

## See Also

### Objects
- [object EnergySaver.Com.apple.EnergySaver.desktop.Schedule.RepeatingPowerOn](./repeatingpoweron-data.dictionary.md)
  The triggers for turning the device on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/energysaver/com.apple.energysaver.desktop.schedule-data.dictionary/repeatingpoweroff-data.dictionary)*