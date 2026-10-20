# createGroup(withIdentifier:name:children:)

**Framework**: Audio Toolbox  
**Kind**: method  
**Role**: Type Method

Creates a parameter group object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
class func createGroup(withIdentifier identifier: String, name: String, children: [AUParameterNode]) -> AUParameterGroup
```

```objc
+ (AUParameterGroup *) createGroupWithIdentifier:(NSString *) identifier name:(NSString *) name children:(NSArray<AUParameterNode *> *) children;
```

#### Return Value

A newly-initialized parameter group object.

## Parameters

- `identifier`: A non-localized, persistent identifier for the group.
- `name`: A localized display name for the group.
- `children`: The group’s child nodes.

## See Also

### Related Documentation
- [class AUParameterGroup](../auparametergroup.md)
  A parameter group object represents a group of related audio unit parameters.
### Audio Unit Implementations
- [class func createParameter(withIdentifier: String, name: String, address: AUParameterAddress, min: AUValue, max: AUValue, unit: AudioUnitParameterUnit, unitName: String?, flags: AudioUnitParameterOptions, valueStrings: [String]?, dependentParameters: [NSNumber]?) -> AUParameter](./createparameter%28withidentifier,name,address,min,max,unit,unitname,flags,valuestrings,dependentparameters%29.md)
  Creates a single parameter object.
- [class func createGroupTemplate([AUParameterNode]) -> AUParameterGroup](./creategrouptemplate%28_%29.md)
  Creates a template group which may be used as a prototype for further group instances.
- [class func createGroup(fromTemplate: AUParameterGroup, identifier: String, name: String, addressOffset: AUParameterAddress) -> AUParameterGroup](./creategroup%28fromtemplate,identifier,name,addressoffset%29.md)
  Initializes a group as a copied instance of a template group.
- [class func createTree(withChildren: [AUParameterNode]) -> AUParameterTree](./createtree%28withchildren%29.md)
  Creates a parameter tree object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparametertree/creategroup(withidentifier:name:children:))*