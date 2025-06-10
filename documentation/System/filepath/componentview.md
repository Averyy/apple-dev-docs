# FilePath.ComponentView

**Framework**: System  
**Kind**: struct

A bidirectional, range replaceable collection of the non-root components that make up a file path.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct ComponentView
```

#### Overview

ComponentView provides access to standard `BidirectionalCollection` algorithms for accessing components from the front or back, as well as standard `RangeReplaceableCollection` algorithms for modifying the file path using component or range of components granularity.

Example:

```swift
var path: FilePath = "/./home/./username/scripts/./tree"
let scriptIdx = path.components.lastIndex(of: "scripts")!
path.components.insert("bin", at: scriptIdx)
// path is "/./home/./username/bin/scripts/./tree"

path.components.removeAll { $0.kind == .currentDirectory }
// path is "/home/username/bin/scripts/tree"
```

## Topics

### Default Implementations
- [BidirectionalCollection Implementations](filepath/componentview/bidirectionalcollection-implementations.md)
- [Collection Implementations](filepath/componentview/collection-implementations.md)
- [Decodable Implementations](filepath/componentview/decodable-implementations.md)
- [Encodable Implementations](filepath/componentview/encodable-implementations.md)
- [Equatable Implementations](filepath/componentview/equatable-implementations.md)
- [Hashable Implementations](filepath/componentview/hashable-implementations.md)
- [RangeReplaceableCollection Implementations](filepath/componentview/rangereplaceablecollection-implementations.md)
- [Sequence Implementations](filepath/componentview/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RangeReplaceableCollection](../Swift/RangeReplaceableCollection.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/componentview)*