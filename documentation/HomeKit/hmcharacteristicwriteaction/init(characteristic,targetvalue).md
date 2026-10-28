# init(characteristic:targetValue:)

**Framework**: HomeKit  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithCharacteristic:(HMCharacteristic *) characteristic targetValue:(TargetValueType) targetValue;
```

## Return Value

A newly initialized characteristic write action object with the specified characteristic and target value.

## Parameters

- `characteristic`: The characteristic.
- `targetValue`: The target value for the characteristic.

## See Also

### Related Documentation
- [HomeKit Developer Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/HomeKitDeveloperGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40015050)
### New Methods
- [var characteristic: HMCharacteristic](./characteristic.md)
  The characteristic whose value is to be written by the action.
- [var targetValue: TargetValueType](./targetvalue.md)
  The value that will be written to the characteristic when the action is executed.
- [func updateTargetValue(TargetValueType, completionHandler: ((any Error)?) -> Void)](./updatetargetvalue%28_,completionhandler%29.md)
  Updates the target value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicwriteaction/init(characteristic:targetvalue:))*