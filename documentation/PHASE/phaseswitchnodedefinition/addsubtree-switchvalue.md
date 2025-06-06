# addSubtree(_:switchValue:)

**Framework**: PHASE  
**Kind**: method

Adds a child node with the given switch value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func addSubtree(_ subtree: PHASESoundEventNodeDefinition, switchValue: String)
```

## Parameters

- `subtree`: The child node, which itself can contain a hierarchical tree of descendent nodes.
- `switchValue`: The meta parameter value that invokes the   child node.

## See Also

- [var switchMetaParameterDefinition: PHASEStringMetaParameterDefinition](phaseswitchnodedefinition/switchmetaparameterdefinition.md)
  The meta parameter that holds the name of the child node to invoke.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseswitchnodedefinition/addsubtree(_:switchvalue:))*