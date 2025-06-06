# AUParameter

**Framework**: Audio Toolbox  
**Kind**: class

An object that represents a single audio unit parameter.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AUParameter
```

## Topics

### Querying Parameter Properties
- [var minValue: AUValue](auparameter/minvalue.md)
  The parameter’s minimum value.
- [var maxValue: AUValue](auparameter/maxvalue.md)
  The parameter’s maximum value.
- [var unit: AudioUnitParameterUnit](auparameter/unit.md)
  The parameter’s unit of measurement.
- [var unitName: String?](auparameter/unitname.md)
  The parameter’s localized unit name.
- [var flags: AudioUnitParameterOptions](auparameter/flags.md)
  The parameter’s characteristic details.
- [var address: AUParameterAddress](auparameter/address.md)
  The parameter’s address.
- [var valueStrings: [String]?](auparameter/valuestrings.md)
  The parameter’s localized value strings.
- [var dependentParameters: [NSNumber]?](auparameter/dependentparameters.md)
  Any other parameter’s whose values may change as a side effect of this parameter’s value changing.
### Managing Parameter Values
- [var value: AUValue](auparameter/value.md)
  The parameter’s current value.
- [func setValue(AUValue, originator: AUParameterObserverToken?)](auparameter/setvalue(_:originator:).md)
  Sets the parameter’s value, avoiding redundant notifications to the originator.
- [func setValue(AUValue, originator: AUParameterObserverToken?, atHostTime: UInt64)](auparameter/setvalue(_:originator:athosttime:).md)
  Sets the parameter’s value, preserving the host time of the gesture that initiated the change.
- [func setValue(AUValue, originator: AUParameterObserverToken?, atHostTime: UInt64, eventType: AUParameterAutomationEventType)](auparameter/setvalue(_:originator:athosttime:eventtype:).md)
- [func string(fromValue: UnsafePointer<AUValue>?) -> String](auparameter/string(fromvalue:).md)
  Gets the string representation of a parameter value.
- [func value(from: String) -> AUValue](auparameter/value(from:).md)
  Converts a string into a parameter value.

## Relationships

### Inherits From
- [AUParameterNode](auparameternode.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class AUParameterGroup](auparametergroup.md)
  A parameter group object represents a group of related audio unit parameters.
- [class AUParameterNode](auparameternode.md)
  An object that represents a node in an audio unit’s parameter tree.
- [class AUParameterTree](auparametertree.md)
  An object that represents a top-level group node that contains all of an audio unit’s parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparameter)*