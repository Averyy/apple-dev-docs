# SetLED

**Framework**: HIDDriverKit  
**Kind**: method

Configures the on/off state for an LED on the device.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
void SetLED(uint32_t usage, bool on);
```

## Parameters

- `usage`: The usage value that matches the LED you want to set. For a list of possible values, see  .
- `on`: A Boolean value that indicates whether to turn the light on or off. Specify   to turn the light on or   to turn it off.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohideventservice/setled)*