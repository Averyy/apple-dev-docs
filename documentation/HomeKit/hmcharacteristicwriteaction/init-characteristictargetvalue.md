# init(characteristic:targetValue:)

**Framework**: HomeKit  
**Kind**: init

Initialize a characteristic write action with a specified characteristic and target value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
init(characteristic: HMCharacteristic, targetValue: TargetValueType)
```

#### Return Value

A newly initialized characteristic write action object with the specified characteristic and target value.

## Parameters

- `characteristic`: The characteristic.
- `targetValue`: The target value for the characteristic.

## See Also

- [HomeKit Developer Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/HomeKitDeveloperGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40015050)
- [var characteristic: HMCharacteristic](hmcharacteristicwriteaction/characteristic.md)
  The characteristic whose value is to be written by the action.
- [var targetValue: TargetValueType](hmcharacteristicwriteaction/targetvalue.md)
  The value that will be written to the characteristic when the action is executed.
- [func updateTargetValue(TargetValueType, completionHandler: ((any Error)?) -> Void)](hmcharacteristicwriteaction/updatetargetvalue(_:completionhandler:).md)
  Updates the target value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicwriteaction/init(characteristic:targetvalue:))*