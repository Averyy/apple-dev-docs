# createGroupTemplate(_:)

**Framework**: Audio Toolbox  
**Kind**: method

Creates a template group which may be used as a prototype for further group instances.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
class func createGroupTemplate(_ children: [AUParameterNode]) -> AUParameterGroup
```

#### Return Value

A newly-initialized parameter group template.

#### Discussion

Template groups provide a way to construct multiple instances of identical parameter groups, sharing certain immutable state between the instances.

Template groups may not appear in trees except at the root.

## Parameters

- `children`: The template group’s child nodes.

## See Also

- [class func createParameter(withIdentifier: String, name: String, address: AUParameterAddress, min: AUValue, max: AUValue, unit: AudioUnitParameterUnit, unitName: String?, flags: AudioUnitParameterOptions, valueStrings: [String]?, dependentParameters: [NSNumber]?) -> AUParameter](auparametertree/createparameter(withidentifier:name:address:min:max:unit:unitname:flags:valuestrings:dependentparameters:).md)
  Creates a single parameter object.
- [class func createGroup(withIdentifier: String, name: String, children: [AUParameterNode]) -> AUParameterGroup](auparametertree/creategroup(withidentifier:name:children:).md)
  Creates a parameter group object.
- [class func createGroup(fromTemplate: AUParameterGroup, identifier: String, name: String, addressOffset: AUParameterAddress) -> AUParameterGroup](auparametertree/creategroup(fromtemplate:identifier:name:addressoffset:).md)
  Initializes a group as a copied instance of a template group.
- [class func createTree(withChildren: [AUParameterNode]) -> AUParameterTree](auparametertree/createtree(withchildren:).md)
  Creates a parameter tree object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparametertree/creategrouptemplate(_:))*