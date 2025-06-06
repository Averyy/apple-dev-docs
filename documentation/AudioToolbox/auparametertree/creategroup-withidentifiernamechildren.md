# createGroup(withIdentifier:name:children:)

**Framework**: Audio Toolbox  
**Kind**: method

Creates a parameter group object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
class func createGroup(withIdentifier identifier: String, name: String, children: [AUParameterNode]) -> AUParameterGroup
```

#### Return Value

A newly-initialized parameter group object.

## Parameters

- `identifier`: A non-localized, persistent identifier for the group.
- `name`: A localized display name for the group.
- `children`: The group’s child nodes.

## See Also

- [class AUParameterGroup](auparametergroup.md)
  A parameter group object represents a group of related audio unit parameters.
- [class func createParameter(withIdentifier: String, name: String, address: AUParameterAddress, min: AUValue, max: AUValue, unit: AudioUnitParameterUnit, unitName: String?, flags: AudioUnitParameterOptions, valueStrings: [String]?, dependentParameters: [NSNumber]?) -> AUParameter](auparametertree/createparameter(withidentifier:name:address:min:max:unit:unitname:flags:valuestrings:dependentparameters:).md)
  Creates a single parameter object.
- [class func createGroupTemplate([AUParameterNode]) -> AUParameterGroup](auparametertree/creategrouptemplate(_:).md)
  Creates a template group which may be used as a prototype for further group instances.
- [class func createGroup(fromTemplate: AUParameterGroup, identifier: String, name: String, addressOffset: AUParameterAddress) -> AUParameterGroup](auparametertree/creategroup(fromtemplate:identifier:name:addressoffset:).md)
  Initializes a group as a copied instance of a template group.
- [class func createTree(withChildren: [AUParameterNode]) -> AUParameterTree](auparametertree/createtree(withchildren:).md)
  Creates a parameter tree object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparametertree/creategroup(withidentifier:name:children:))*