# AUParameterGroup

**Framework**: Audio Toolbox  
**Kind**: class

A parameter group object represents a group of related audio unit parameters.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AUParameterGroup
```

#### Overview

A parameter group is KVC-compliant for its children. For example, calling the parameter group’s [`value(forKey:)`](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/value(forkey:)) method, with a key value of *volume*, returns a child whose [`identifier`](auparameternode/identifier.md) value matches that key.

## Topics

### Obtaining Group Parameters
- [var allParameters: [AUParameter]](auparametergroup/allparameters.md)
  Returns a flat array of all parameters in the group, including those in child groups.
- [var children: [AUParameterNode]](auparametergroup/children.md)
  The group’s child nodes.
### Initializers
- [init?(coder: NSCoder)](auparametergroup/init(coder:).md)

## Relationships

### Inherits From
- [AUParameterNode](auparameternode.md)
### Inherited By
- [AUParameterTree](auparametertree.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class AUParameter](auparameter.md)
  An object that represents a single audio unit parameter.
- [class AUParameterNode](auparameternode.md)
  An object that represents a node in an audio unit’s parameter tree.
- [class AUParameterTree](auparametertree.md)
  An object that represents a top-level group node that contains all of an audio unit’s parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparametergroup)*