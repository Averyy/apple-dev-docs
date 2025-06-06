# value(from:)

**Framework**: Audio Toolbox  
**Kind**: method

Converts a string into a parameter value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func value(from string: String) -> AUValue
```

#### Return Value

The parameter value obtained from the string.

## Parameters

- `string`: The string representation of a parameter value.

## See Also

- [var value: AUValue](auparameter/value.md)
  The parameter’s current value.
- [func setValue(AUValue, originator: AUParameterObserverToken?)](auparameter/setvalue(_:originator:).md)
  Sets the parameter’s value, avoiding redundant notifications to the originator.
- [func setValue(AUValue, originator: AUParameterObserverToken?, atHostTime: UInt64)](auparameter/setvalue(_:originator:athosttime:).md)
  Sets the parameter’s value, preserving the host time of the gesture that initiated the change.
- [func setValue(AUValue, originator: AUParameterObserverToken?, atHostTime: UInt64, eventType: AUParameterAutomationEventType)](auparameter/setvalue(_:originator:athosttime:eventtype:).md)
- [func string(fromValue: UnsafePointer<AUValue>?) -> String](auparameter/string(fromvalue:).md)
  Gets the string representation of a parameter value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparameter/value(from:))*