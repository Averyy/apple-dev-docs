# createIndicator(_:min:max:currentValue:)

**Framework**: IOBluetooth  
**Kind**: method

Sends a request to the Bluetooth device to show or update a status indicator.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func createIndicator(_ indicatorName: String!, min minValue: Int32, max maxValue: Int32, currentValue: Int32)
```

## Parameters

- `indicatorName`: The name of the indicator. Use one of the following constants:
- `minValue`: The minimum value for the indicator.
- `maxValue`: The maximum value for the indicator.
- `currentValue`: The current value of the indicator.

## See Also

- [Status Indicator Constants](status-indicator-constants.md)
  Send commands to modify the status indicators of a hands-free Bluetooth device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogateway/createindicator(_:min:max:currentvalue:))*