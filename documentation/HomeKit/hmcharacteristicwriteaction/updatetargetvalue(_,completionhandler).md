# updateTargetValue(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Updates the target value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func updateTargetValue(_ targetValue: TargetValueType, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func updateTargetValue(_ targetValue: TargetValueType) async throws
```

```objc
- (void) updateTargetValue:(TargetValueType) targetValue completionHandler:(void (^)(NSError *error)) completion;
```

## Parameters

- `targetValue`: The new target value.
- `completion`: The block executed after the request is processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### New Methods
- [init(characteristic: HMCharacteristic, targetValue: TargetValueType)](./init%28characteristic,targetvalue%29.md)
  Initialize a characteristic write action with a specified characteristic and target value.
- [var characteristic: HMCharacteristic](./characteristic.md)
  The characteristic whose value is to be written by the action.
- [var targetValue: TargetValueType](./targetvalue.md)
  The value that will be written to the characteristic when the action is executed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicwriteaction/updatetargetvalue(_:completionhandler:))*