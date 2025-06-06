# addSubtree(_:weight:)

**Framework**: PHASE  
**Kind**: method

Adds a node tree that’s one of the random-selection options.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func addSubtree(_ subtree: PHASESoundEventNodeDefinition, weight: NSNumber)
```

## Parameters

- `subtree`: The child node, which itself can contain a hierarchical tree of descendent nodes.
- `weight`: A number that implements favoritism in the random selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaserandomnodedefinition/addsubtree(_:weight:))*