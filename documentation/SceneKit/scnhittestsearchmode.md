# SCNHitTestSearchMode

**Framework**: SceneKit  
**Kind**: enum

Possible values for the [`searchMode`](scnhittestoption/searchmode.md) option used with hit-testing methods.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum SCNHitTestSearchMode
```

## Topics

### Search Modes
- [SCNHitTestSearchMode.all](scnhittestsearchmode/all.md)
  The hit test should return all possible results, sorted from nearest to farthest.
- [SCNHitTestSearchMode.any](scnhittestsearchmode/any.md)
  The hit test should return only the first object found, regardless of distance.
- [SCNHitTestSearchMode.closest](scnhittestsearchmode/closest.md)
  The hit test should return only the closes object found.
### Initializers
- [init?(rawValue: Int)](scnhittestsearchmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static let backFaceCulling: SCNHitTestOption](scnhittestoption/backfaceculling.md)
  An option to ignore faces not oriented toward the camera.
- [static let boundingBoxOnly: SCNHitTestOption](scnhittestoption/boundingboxonly.md)
  An option to search for objects by bounding box only.
- [static let categoryBitMask: SCNHitTestOption](scnhittestoption/categorybitmask.md)
  An option to search only for objects matching a specified bitmask.
- [static let clipToZRange: SCNHitTestOption](scnhittestoption/cliptozrange.md)
  An option to search for objects only within the depth range of the current point of view.
- [static let ignoreChildNodes: SCNHitTestOption](scnhittestoption/ignorechildnodes.md)
  An option to ignore child nodes when searching.
- [static let ignoreHiddenNodes: SCNHitTestOption](scnhittestoption/ignorehiddennodes.md)
  An option to ignore hidden nodes when searching.
- [static let rootNode: SCNHitTestOption](scnhittestoption/rootnode.md)
  The root of the node hierarchy to be searched.
- [static let searchMode: SCNHitTestOption](scnhittestoption/searchmode.md)
  An option for the number and order of hit test results to provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnhittestsearchmode)*