# SetLED

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Configures the on/off state for an LED on the device.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual void SetLED(uint32_t usage, bool on);
```

## Parameters

- `usage`: The usage value that matches the LED you want to set. For a list of possible values, see [LEDs](../leds-enum.md).
- `on`: A Boolean value that indicates whether to turn the light on or off. Specify `true` to turn the light on or `false` to turn it off.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohideventservice/setled)*