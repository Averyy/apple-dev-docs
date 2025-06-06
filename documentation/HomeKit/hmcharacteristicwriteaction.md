# HMCharacteristicWriteAction

**Framework**: HomeKit  
**Kind**: class

An action in an action set that writes a value to a characteristic.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HMCharacteristicWriteAction<TargetValueType> where TargetValueType : NSCopying
```

#### Overview

Action sets are instances of [`HMActionSet`](hmactionset.md).

## Topics

### New Methods
- [init(characteristic: HMCharacteristic, targetValue: TargetValueType)](hmcharacteristicwriteaction/init(characteristic:targetvalue:).md)
  Initialize a characteristic write action with a specified characteristic and target value.
- [var characteristic: HMCharacteristic](hmcharacteristicwriteaction/characteristic.md)
  The characteristic whose value is to be written by the action.
- [var targetValue: TargetValueType](hmcharacteristicwriteaction/targetvalue.md)
  The value that will be written to the characteristic when the action is executed.
- [func updateTargetValue(TargetValueType, completionHandler: ((any Error)?) -> Void)](hmcharacteristicwriteaction/updatetargetvalue(_:completionhandler:).md)
  Updates the target value.

## Relationships

### Inherits From
- [HMAction](hmaction.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var actions: Set<HMAction>](hmactionset/actions.md)
  Set of actions in the action set.
- [func addAction(HMAction, completionHandler: HMErrorBlock)](hmactionset/addaction(_:completionhandler:).md)
  Adds an action to the action set.
- [func removeAction(HMAction, completionHandler: HMErrorBlock)](hmactionset/removeaction(_:completionhandler:).md)
  Removes an action from the action set.
- [class HMAction](hmaction.md)
  An abstract base class for actions in HomeKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicwriteaction)*