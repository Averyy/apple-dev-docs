# updateTargetValue(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Updates the target value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func updateTargetValue(_ targetValue: TargetValueType) async throws
```

## Parameters

- `targetValue`: The new target value.
- `completion`: The block executed after the request is processed.

## See Also

- [init(characteristic: HMCharacteristic, targetValue: TargetValueType)](hmcharacteristicwriteaction/init(characteristic:targetvalue:).md)
  Initialize a characteristic write action with a specified characteristic and target value.
- [var characteristic: HMCharacteristic](hmcharacteristicwriteaction/characteristic.md)
  The characteristic whose value is to be written by the action.
- [var targetValue: TargetValueType](hmcharacteristicwriteaction/targetvalue.md)
  The value that will be written to the characteristic when the action is executed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicwriteaction/updatetargetvalue(_:completionhandler:))*