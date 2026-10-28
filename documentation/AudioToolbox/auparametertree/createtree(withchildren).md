# createTree(withChildren:)

**Framework**: Audio Toolbox  
**Kind**: method  
**Role**: Type Method

Creates a parameter tree object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
class func createTree(withChildren children: [AUParameterNode]) -> AUParameterTree
```

```objc
+ (AUParameterTree *) createTreeWithChildren:(NSArray<AUParameterNode *> *) children;
```

## Return Value

A newly-initialized parameter tree object.

## Parameters

- `children`: The tree’s top-level children nodes.

## See Also

### Related Documentation
- [class AUParameterTree](../auparametertree.md)
  An object that represents a top-level group node that contains all of an audio unit’s parameters.
### Audio Unit Implementations
- [class func createParameter(withIdentifier: String, name: String, address: AUParameterAddress, min: AUValue, max: AUValue, unit: AudioUnitParameterUnit, unitName: String?, flags: AudioUnitParameterOptions, valueStrings: [String]?, dependentParameters: [NSNumber]?) -> AUParameter](./createparameter%28withidentifier,name,address,min,max,unit,unitname,flags,valuestrings,dependentparameters%29.md)
  Creates a single parameter object.
- [class func createGroup(withIdentifier: String, name: String, children: [AUParameterNode]) -> AUParameterGroup](./creategroup%28withidentifier,name,children%29.md)
  Creates a parameter group object.
- [class func createGroupTemplate([AUParameterNode]) -> AUParameterGroup](./creategrouptemplate%28_%29.md)
  Creates a template group which may be used as a prototype for further group instances.
- [class func createGroup(fromTemplate: AUParameterGroup, identifier: String, name: String, addressOffset: AUParameterAddress) -> AUParameterGroup](./creategroup%28fromtemplate,identifier,name,addressoffset%29.md)
  Initializes a group as a copied instance of a template group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparametertree/createtree(withchildren:))*