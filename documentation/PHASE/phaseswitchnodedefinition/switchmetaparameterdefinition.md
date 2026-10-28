# switchMetaParameterDefinition

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

The meta parameter that holds the name of the child node to invoke.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var switchMetaParameterDefinition: PHASEStringMetaParameterDefinition { get }
```

```objc
@property (nonatomic, strong, readonly) PHASEStringMetaParameterDefinition * switchMetaParameterDefinition;
```

## Discussion

The framework sets the value of this property to the [`init(switchMetaParameterDefinition:)`](./init%28switchmetaparameterdefinition%29.md) argument.

## See Also

### Managing Child Nodes
- [func addSubtree(PHASESoundEventNodeDefinition, switchValue: String)](./addsubtree%28_,switchvalue%29.md)
  Adds a child node with the given switch value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseswitchnodedefinition/switchmetaparameterdefinition)*