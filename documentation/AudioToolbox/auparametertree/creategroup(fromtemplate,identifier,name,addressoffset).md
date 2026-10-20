# createGroup(fromTemplate:identifier:name:addressOffset:)

**Framework**: Audio Toolbox  
**Kind**: method  
**Role**: Type Method

Initializes a group as a copied instance of a template group.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
class func createGroup(fromTemplate templateGroup: AUParameterGroup, identifier: String, name: String, addressOffset: AUParameterAddress) -> AUParameterGroup
```

```objc
+ (AUParameterGroup *) createGroupFromTemplate:(AUParameterGroup *) templateGroup identifier:(NSString *) identifier name:(NSString *) name addressOffset:(AUParameterAddress) addressOffset;
```

#### Return Value

A newly-initialized parameter group object.

## Parameters

- `templateGroup`: A group to be used as a template and largely copied from.
- `identifier`: A non-localized, persistent identifier for the new group.
- `name`: A localized display name for the new group.
- `addressOffset`: The address offset for the new group’s parameters, with respect to the template group.

## See Also

### Audio Unit Implementations
- [class func createParameter(withIdentifier: String, name: String, address: AUParameterAddress, min: AUValue, max: AUValue, unit: AudioUnitParameterUnit, unitName: String?, flags: AudioUnitParameterOptions, valueStrings: [String]?, dependentParameters: [NSNumber]?) -> AUParameter](./createparameter%28withidentifier,name,address,min,max,unit,unitname,flags,valuestrings,dependentparameters%29.md)
  Creates a single parameter object.
- [class func createGroup(withIdentifier: String, name: String, children: [AUParameterNode]) -> AUParameterGroup](./creategroup%28withidentifier,name,children%29.md)
  Creates a parameter group object.
- [class func createGroupTemplate([AUParameterNode]) -> AUParameterGroup](./creategrouptemplate%28_%29.md)
  Creates a template group which may be used as a prototype for further group instances.
- [class func createTree(withChildren: [AUParameterNode]) -> AUParameterTree](./createtree%28withchildren%29.md)
  Creates a parameter tree object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparametertree/creategroup(fromtemplate:identifier:name:addressoffset:))*