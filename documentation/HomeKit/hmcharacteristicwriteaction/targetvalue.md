# targetValue

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, readonly) TargetValueType targetValue;
```

## See Also

### New Methods
- [init(characteristic: HMCharacteristic, targetValue: TargetValueType)](./init%28characteristic,targetvalue%29.md)
  Initialize a characteristic write action with a specified characteristic and target value.
- [var characteristic: HMCharacteristic](./characteristic.md)
  The characteristic whose value is to be written by the action.
- [func updateTargetValue(TargetValueType, completionHandler: ((any Error)?) -> Void)](./updatetargetvalue%28_,completionhandler%29.md)
  Updates the target value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicwriteaction/targetvalue)*