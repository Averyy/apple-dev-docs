# EnergySaver.Com.apple.EnergySaver.portable.ACPower

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

The laptop AC power Energy Saver settings.

**Availability**:
- macOS 10.7+

## Declaration

```
object EnergySaver.Com.apple.EnergySaver.portable.ACPower
```

## Properties

- `Automatic Restart On Power Loss` (integer): If `true`, enables “Start up automatically after a power failure.”

  **Allowed Values**: `0`, `1`
- `Disk Sleep Timer` (integer): The disk sleep time, in minutes. A value of 0 means never.

  **Minimum**: `0`; **Maximum**: `180`
- `Display Sleep Timer` (integer): The display sleep time, in minutes. A value of 0 means never.

  **Minimum**: `0`; **Maximum**: `180`
- `Dynamic Power Step` (integer): May not be available on all systems.

  **Allowed Values**: `0`, `1`
- `Reduce Processor Speed` (integer): May not be available on all systems.

  **Allowed Values**: `0`, `1`
- `System Sleep Timer` (integer): System sleep time, in minutes. A value of 0 means never.

  **Minimum**: `0`; **Maximum**: `180`
- `Wake on LAN` (integer): If `true`, enables “Wake for network access.”

  **Allowed Values**: `0`, `1`
- `Wake On Modem Ring` (integer): If `true`, enables “Wake for modem ring.”

  **Allowed Values**: `0`, `1`

## See Also

### Objects
- [object EnergySaver.Com.apple.EnergySaver.desktop.ACPower](./com.apple.energysaver.desktop.acpower-data.dictionary.md)
  The desktop AC power Energy Saver settings.
- [object EnergySaver.Com.apple.EnergySaver.desktop.Schedule](./com.apple.energysaver.desktop.schedule-data.dictionary.md)
  The schedule for turning the device on or off.
- [object EnergySaver.Com.apple.EnergySaver.portable.BatteryPower](./com.apple.energysaver.portable.batterypower-data.dictionary.md)
  The laptop battery power Energy Saver settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/energysaver/com.apple.energysaver.portable.acpower-data.dictionary)*