# FilePath.ComponentView

**Framework**: System  
**Kind**: struct  
**Role**: Structure

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

## Relationships

### Conforms To
- [BidirectionalCollection](../../Swift/bidirectionalcollection.md)
- [Collection](../../Swift/collection.md)
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RangeReplaceableCollection](../../Swift/rangereplaceablecollection.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [Sequence](../../Swift/sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/componentview)*