# setValue(_:originator:atHostTime:)

**Framework**: Audio Toolbox  
**Kind**: method  
**Role**: Instance Method

Sets the parameter’s value, preserving the host time of the gesture that initiated the change.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setValue(_ value: AUValue, originator: AUParameterObserverToken?, atHostTime hostTime: UInt64)
```

```objc
- (void) setValue:(AUValue) value originator:(AUParameterObserverToken) originator atHostTime:(uint64_t) hostTime;
```

## Parameters

- `value`: The parameter’s new value.
- `originator`: The originator of the change in value. This token allows for observer management to avoid notification callback loops.
- `hostTime`: The time at which to schedule the change in value. This parameter allows for synchronization with other events.

## See Also

### Managing Parameter Values
- [var value: AUValue](./value.md)
  The parameter’s current value.
- [func setValue(AUValue, originator: AUParameterObserverToken?)](./setvalue%28_,originator%29.md)
  Sets the parameter’s value, avoiding redundant notifications to the originator.
- [func setValue(AUValue, originator: AUParameterObserverToken?, atHostTime: UInt64, eventType: AUParameterAutomationEventType)](./setvalue%28_,originator,athosttime,eventtype%29.md)
- [func string(fromValue: UnsafePointer<AUValue>?) -> String](./string%28fromvalue%29.md)
  Gets the string representation of a parameter value.
- [func value(from: String) -> AUValue](./value%28from%29.md)
  Converts a string into a parameter value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparameter/setvalue(_:originator:athosttime:))*