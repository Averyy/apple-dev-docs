# setIndicator(_:value:)

**Framework**: IOBluetooth  
**Kind**: method

Set an indicator’s value

**Availability**:
- macOS 10.7+

## Declaration

```swift
func setIndicator(_ indicatorName: String!, value indicatorValue: Int32)
```

#### Discussion

Sets an indicator’s value.

## Parameters

- `indicatorName`: See “Hands free indicator constants,” for standard indicator names.
- `indicatorValue`: Will set the indicator value as long as it is within the min and max values allowed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/setindicator(_:value:))*