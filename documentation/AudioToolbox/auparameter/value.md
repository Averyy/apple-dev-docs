# value

**Framework**: Audio Toolbox  
**Kind**: property

The parameter’s current value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var value: AUValue { get set }
```

## See Also

- [func setValue(AUValue, originator: AUParameterObserverToken?)](auparameter/setvalue(_:originator:).md)
  Sets the parameter’s value, avoiding redundant notifications to the originator.
- [func setValue(AUValue, originator: AUParameterObserverToken?, atHostTime: UInt64)](auparameter/setvalue(_:originator:athosttime:).md)
  Sets the parameter’s value, preserving the host time of the gesture that initiated the change.
- [func setValue(AUValue, originator: AUParameterObserverToken?, atHostTime: UInt64, eventType: AUParameterAutomationEventType)](auparameter/setvalue(_:originator:athosttime:eventtype:).md)
- [func string(fromValue: UnsafePointer<AUValue>?) -> String](auparameter/string(fromvalue:).md)
  Gets the string representation of a parameter value.
- [func value(from: String) -> AUValue](auparameter/value(from:).md)
  Converts a string into a parameter value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparameter/value)*