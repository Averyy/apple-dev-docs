# SCNHitTestOption

**Framework**: SceneKit  
**Kind**: struct

Options affecting the behavior of SceneKit hit-testing methods.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct SCNHitTestOption
```

## Topics

### Options
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
- [enum SCNHitTestSearchMode](scnhittestsearchmode.md)
  Possible values for the [`searchMode`](scnhittestoption/searchmode.md) option used with hit-testing methods.
### Deprecated
- [static let firstFoundOnly: SCNHitTestOption](scnhittestoption/firstfoundonly.md)
  An option to return only the first object found.
- [static let sortResults: SCNHitTestOption](scnhittestoption/sortresults.md)
  An option to sort the results of a hit-test.
### Initializers
- [init(rawValue: String)](scnhittestoption/init(rawvalue:).md)
### Type Properties
- [static let ignoreLightArea: SCNHitTestOption](scnhittestoption/ignorelightarea.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func hitTestWithSegment(from: SCNVector3, to: SCNVector3, options: [String : Any]?) -> [SCNHitTestResult]](scnnode/hittestwithsegment(from:to:options:).md)
  Searches the node’s child node subtree for objects intersecting a line segment between two specified points.
- [func hitTestWithSegment(from: SCNVector3, to: SCNVector3, options: [String : Any]?) -> [SCNHitTestResult]](scnnode/hittestwithsegment(from:to:options:).md)
  Searches the node’s child node subtree for objects intersecting a line segment between two specified points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnhittestoption)*