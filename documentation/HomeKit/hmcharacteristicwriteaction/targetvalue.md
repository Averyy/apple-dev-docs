# targetValue

**Framework**: HomeKit  
**Kind**: property

The value that will be written to the characteristic when the action is executed.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var targetValue: TargetValueType { get }
```

## See Also

- [init(characteristic: HMCharacteristic, targetValue: TargetValueType)](hmcharacteristicwriteaction/init(characteristic:targetvalue:).md)
  Initialize a characteristic write action with a specified characteristic and target value.
- [var characteristic: HMCharacteristic](hmcharacteristicwriteaction/characteristic.md)
  The characteristic whose value is to be written by the action.
- [func updateTargetValue(TargetValueType, completionHandler: ((any Error)?) -> Void)](hmcharacteristicwriteaction/updatetargetvalue(_:completionhandler:).md)
  Updates the target value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicwriteaction/targetvalue)*