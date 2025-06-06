# setValue(_:originator:)

**Framework**: Audio Toolbox  
**Kind**: method

Sets the parameter’s value, avoiding redundant notifications to the originator.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setValue(_ value: AUValue, originator: AUParameterObserverToken?)
```

## Parameters

- `value`: The parameter’s new value.
- `originator`: The originator of the change in value. This token allows for observer management to avoid notification callback loops.

## See Also

- [var value: AUValue](auparameter/value.md)
  The parameter’s current value.
- [func setValue(AUValue, originator: AUParameterObserverToken?, atHostTime: UInt64)](auparameter/setvalue(_:originator:athosttime:).md)
  Sets the parameter’s value, preserving the host time of the gesture that initiated the change.
- [func setValue(AUValue, originator: AUParameterObserverToken?, atHostTime: UInt64, eventType: AUParameterAutomationEventType)](auparameter/setvalue(_:originator:athosttime:eventtype:).md)
- [func string(fromValue: UnsafePointer<AUValue>?) -> String](auparameter/string(fromvalue:).md)
  Gets the string representation of a parameter value.
- [func value(from: String) -> AUValue](auparameter/value(from:).md)
  Converts a string into a parameter value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparameter/setvalue(_:originator:))*