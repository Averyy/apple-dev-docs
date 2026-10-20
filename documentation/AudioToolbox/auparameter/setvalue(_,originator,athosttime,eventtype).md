# setValue(_:originator:atHostTime:eventType:)

**Framework**: Audio Toolbox  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func setValue(_ value: AUValue, originator: AUParameterObserverToken?, atHostTime hostTime: UInt64, eventType: AUParameterAutomationEventType)
```

```objc
- (void) setValue:(AUValue) value originator:(AUParameterObserverToken) originator atHostTime:(uint64_t) hostTime eventType:(AUParameterAutomationEventType) eventType;
```

## See Also

### Managing Parameter Values
- [var value: AUValue](./value.md)
  The parameter’s current value.
- [func setValue(AUValue, originator: AUParameterObserverToken?)](./setvalue%28_,originator%29.md)
  Sets the parameter’s value, avoiding redundant notifications to the originator.
- [func setValue(AUValue, originator: AUParameterObserverToken?, atHostTime: UInt64)](./setvalue%28_,originator,athosttime%29.md)
  Sets the parameter’s value, preserving the host time of the gesture that initiated the change.
- [func string(fromValue: UnsafePointer<AUValue>?) -> String](./string%28fromvalue%29.md)
  Gets the string representation of a parameter value.
- [func value(from: String) -> AUValue](./value%28from%29.md)
  Converts a string into a parameter value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparameter/setvalue(_:originator:athosttime:eventtype:))*