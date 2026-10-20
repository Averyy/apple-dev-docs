# SetLED

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the state of an LED on the device.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual void SetLED(uint32_t usage, bool on);
```

## Parameters

- `usage`: The LED to set. Specify a value from the LED usage tables in [LEDs](../leds-enum.md).
- `on`: A Boolean value that indicates whether to turn the LED on or off. Specify `true` to turn the LED on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventdriver/setled)*