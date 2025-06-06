# string(fromValue:)

**Framework**: Audio Toolbox  
**Kind**: method

Gets the string representation of a parameter value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func string(fromValue value: UnsafePointer<AUValue>?) -> String
```

#### Return Value

The string representation of a parameter value.

#### Discussion

Pass `nil` into the `value` parameter to use the current value.

## Parameters

- `value`: The parameter value to represent as a string.

## See Also

- [var value: AUValue](auparameter/value.md)
  The parameter’s current value.
- [func setValue(AUValue, originator: AUParameterObserverToken?)](auparameter/setvalue(_:originator:).md)
  Sets the parameter’s value, avoiding redundant notifications to the originator.
- [func setValue(AUValue, originator: AUParameterObserverToken?, atHostTime: UInt64)](auparameter/setvalue(_:originator:athosttime:).md)
  Sets the parameter’s value, preserving the host time of the gesture that initiated the change.
- [func setValue(AUValue, originator: AUParameterObserverToken?, atHostTime: UInt64, eventType: AUParameterAutomationEventType)](auparameter/setvalue(_:originator:athosttime:eventtype:).md)
- [func value(from: String) -> AUValue](auparameter/value(from:).md)
  Converts a string into a parameter value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparameter/string(fromvalue:))*