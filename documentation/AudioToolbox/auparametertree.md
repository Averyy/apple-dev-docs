# AUParameterTree

**Framework**: Audio Toolbox  
**Kind**: class

An object that represents a top-level group node that contains all of an audio unit’s parameters.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AUParameterTree
```

#### Overview

An audio unit’s parameters are organized into a tree containing groups and parameters (groups may be nested).

The parameter tree is KVO-compliant. An audio unit may choose to dynamically rearrange the tree; when doing so, it must issue a KVO notification on the audio unit’s [`parameterTree`](auaudiounit/parametertree.md) property.

## Topics

### Obtaining Tree Parameters
- [func parameter(withAddress: AUParameterAddress) -> AUParameter?](auparametertree/parameter(withaddress:).md)
  Searches the tree for a parameter with a specific address.
- [func parameter(withID: AudioUnitParameterID, scope: AudioUnitScope, element: AudioUnitElement) -> AUParameter?](auparametertree/parameter(withid:scope:element:).md)
  Searches the tree for a specific version 2 audio unit parameter.
### Audio Unit Implementations
- [class func createParameter(withIdentifier: String, name: String, address: AUParameterAddress, min: AUValue, max: AUValue, unit: AudioUnitParameterUnit, unitName: String?, flags: AudioUnitParameterOptions, valueStrings: [String]?, dependentParameters: [NSNumber]?) -> AUParameter](auparametertree/createparameter(withidentifier:name:address:min:max:unit:unitname:flags:valuestrings:dependentparameters:).md)
  Creates a single parameter object.
- [class func createGroup(withIdentifier: String, name: String, children: [AUParameterNode]) -> AUParameterGroup](auparametertree/creategroup(withidentifier:name:children:).md)
  Creates a parameter group object.
- [class func createGroupTemplate([AUParameterNode]) -> AUParameterGroup](auparametertree/creategrouptemplate(_:).md)
  Creates a template group which may be used as a prototype for further group instances.
- [class func createGroup(fromTemplate: AUParameterGroup, identifier: String, name: String, addressOffset: AUParameterAddress) -> AUParameterGroup](auparametertree/creategroup(fromtemplate:identifier:name:addressoffset:).md)
  Initializes a group as a copied instance of a template group.
- [class func createTree(withChildren: [AUParameterNode]) -> AUParameterTree](auparametertree/createtree(withchildren:).md)
  Creates a parameter tree object.

## Relationships

### Inherits From
- [AUParameterGroup](auparametergroup.md)
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

- [class AUParameter](auparameter.md)
  An object that represents a single audio unit parameter.
- [class AUParameterGroup](auparametergroup.md)
  A parameter group object represents a group of related audio unit parameters.
- [class AUParameterNode](auparameternode.md)
  An object that represents a node in an audio unit’s parameter tree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparametertree)*