# children

**Framework**: PHASE  
**Kind**: property

An array of child sound event nodes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var children: [PHASESoundEventNodeDefinition] { get }
```

#### Discussion

To add children, use the add subtree functions of the derived class. For example, add children to a container node using [`addSubtree(_:)`](phasecontainernodedefinition/addsubtree(_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundeventnodedefinition/children)*