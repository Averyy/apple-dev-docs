# SetLED

**Framework**: HIDDriverKit  
**Kind**: method

Sets the state of an LED on the device.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
void SetLED(uint32_t usage, bool on);
```

## Parameters

- `usage`: The LED to set. Specify a value from the LED usage tables in  .
- `on`: A Boolean value that indicates whether to turn the LED on or off. Specify   to turn the LED on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventdriver/setled)*