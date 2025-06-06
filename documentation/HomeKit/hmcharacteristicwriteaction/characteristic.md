# characteristic

**Framework**: HomeKit  
**Kind**: property

The characteristic whose value is to be written by the action.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var characteristic: HMCharacteristic { get }
```

## See Also

- [init(characteristic: HMCharacteristic, targetValue: TargetValueType)](hmcharacteristicwriteaction/init(characteristic:targetvalue:).md)
  Initialize a characteristic write action with a specified characteristic and target value.
- [var targetValue: TargetValueType](hmcharacteristicwriteaction/targetvalue.md)
  The value that will be written to the characteristic when the action is executed.
- [func updateTargetValue(TargetValueType, completionHandler: ((any Error)?) -> Void)](hmcharacteristicwriteaction/updatetargetvalue(_:completionhandler:).md)
  Updates the target value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicwriteaction/characteristic)*