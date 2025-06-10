# isLoaded

**Framework**: SceneKit  
**Kind**: property

A Boolean value that indicates whether the reference node has already loaded its content.

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
@MainActor
var isLoaded: Bool { get }
```

## See Also

- [var referenceURL: URL](scnreferencenode/referenceurl.md)
  The URL to a scene file from which to load content for the reference node.
- [var loadingPolicy: SCNReferenceLoadingPolicy](scnreferencenode/loadingpolicy.md)
  An option for whether to load the node’s content automatically.
- [func load()](scnreferencenode/load.md)
  Loads content into the node from its referenced external scene file.
- [func unload()](scnreferencenode/unload.md)
  Removes the node’s children and marks the node as not loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnreferencenode/isloaded)*