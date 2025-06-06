# referenceURL

**Framework**: SceneKit  
**Kind**: property

The URL to a scene file from which to load content for the reference node.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@MainActor
var referenceURL: URL { get set }
```

#### Discussion

When the reference node loads its content (either automatically, according to the [`loadingPolicy`](scnreferencenode/loadingpolicy.md) property, or when you call the [`load()`](scnreferencenode/load().md) method), SceneKit loads the referenced scene file. All children of the scene file’s root node become children of the reference node.

## See Also

- [var loadingPolicy: SCNReferenceLoadingPolicy](scnreferencenode/loadingpolicy.md)
  An option for whether to load the node’s content automatically.
- [func load()](scnreferencenode/load.md)
  Loads content into the node from its referenced external scene file.
- [var isLoaded: Bool](scnreferencenode/isloaded.md)
  A Boolean value that indicates whether the reference node has already loaded its content.
- [func unload()](scnreferencenode/unload.md)
  Removes the node’s children and marks the node as not loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnreferencenode/referenceurl)*