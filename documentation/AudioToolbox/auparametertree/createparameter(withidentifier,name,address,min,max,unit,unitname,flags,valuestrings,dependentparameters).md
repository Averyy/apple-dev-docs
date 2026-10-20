# createParameter(withIdentifier:name:address:min:max:unit:unitName:flags:valueStrings:dependentParameters:)

**Framework**: Audio Toolbox  
**Kind**: method

Creates a single parameter object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
class func createParameter(withIdentifier identifier: String, name: String, address: AUParameterAddress, min: AUValue, max: AUValue, unit: AudioUnitParameterUnit, unitName: String?, flags: AudioUnitParameterOptions = [], valueStrings: [String]?, dependentParameters: [NSNumber]?) -> AUParameter
```

#### Return Value

A newly-initialized parameter object.

## Parameters

- `identifier`: The parameter’s non-localized, permanent name.
- `name`: The parameter’s localized name for display.
- `address`: The parameter’s address.
- `min`: The parameter’s minimum value.
- `max`: The parameter’s maximum value.
- `unit`: The parameter’s unit of measurement.
- `unitName`: The parameter’s localized unit name.
- `flags`: The parameter’s characteristic details.
- `valueStrings`: The parameter’s localized value strings.
- `dependentParameters`: Any other parameter’s whose values may change as a side effect of this parameter’s value changing.

## See Also

- [class AUParameter](auparameter.md)
  An object that represents a single audio unit parameter.
- [class func createGroup(withIdentifier: String, name: String, children: [AUParameterNode]) -> AUParameterGroup](auparametertree/creategroup(withidentifier:name:children:).md)
  Creates a parameter group object.
- [class func createGroupTemplate([AUParameterNode]) -> AUParameterGroup](auparametertree/creategrouptemplate(_:).md)
  Creates a template group which may be used as a prototype for further group instances.
- [class func createGroup(fromTemplate: AUParameterGroup, identifier: String, name: String, addressOffset: AUParameterAddress) -> AUParameterGroup](auparametertree/creategroup(fromtemplate:identifier:name:addressoffset:).md)
  Initializes a group as a copied instance of a template group.
- [class func createTree(withChildren: [AUParameterNode]) -> AUParameterTree](auparametertree/createtree(withchildren:).md)
  Creates a parameter tree object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparametertree/createparameter(withidentifier:name:address:min:max:unit:unitname:flags:valuestrings:dependentparameters:))*