# children

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly) NSArray<PHASESoundEventNodeDefinition *> * children;
```

## Discussion

To add children, use the add subtree functions of the derived class. For example, add children to a container node using [`addSubtree(_:)`](../phasecontainernodedefinition/addsubtree%28_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundeventnodedefinition/children)*