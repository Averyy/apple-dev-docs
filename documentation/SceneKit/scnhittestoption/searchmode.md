# searchMode

**Framework**: SceneKit  
**Kind**: property

An option for the number and order of hit test results to provide.

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
static let searchMode: SCNHitTestOption
```

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing the raw integer value of an [`SCNHitTestSearchMode`](scnhittestsearchmode.md) constant.

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
- [enum SCNHitTestSearchMode](scnhittestsearchmode.md)
  Possible values for the [`searchMode`](scnhittestoption/searchmode.md) option used with hit-testing methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnhittestoption/searchmode)*