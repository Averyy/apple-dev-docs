# loadingPolicy

**Framework**: SceneKit  
**Kind**: property

An option for whether to load the node’s content automatically.

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
var loadingPolicy: SCNReferenceLoadingPolicy { get set }
```

#### Discussion

If this property’s value is [`SCNReferenceLoadingPolicy.immediate`](scnreferenceloadingpolicy/immediate.md) (the default), instantiating a reference node from an archive (using the [`NSKeyedUnarchiver`](https://developer.apple.com/documentation/Foundation/NSKeyedUnarchiver) class) automatically loads the node’s external content. Set this property to [`SCNReferenceLoadingPolicy.onDemand`](scnreferenceloadingpolicy/ondemand.md) before archiving an [`SCNReferenceNode`](scnreferencenode.md) object if you don’t want that reference node to automatically load its content when unarchived. In that case, call the [`load()`](scnreferencenode/load().md) method after unarchiving when you want to load the node’s content.

## See Also

- [var referenceURL: URL](scnreferencenode/referenceurl.md)
  The URL to a scene file from which to load content for the reference node.
- [func load()](scnreferencenode/load.md)
  Loads content into the node from its referenced external scene file.
- [var isLoaded: Bool](scnreferencenode/isloaded.md)
  A Boolean value that indicates whether the reference node has already loaded its content.
- [func unload()](scnreferencenode/unload.md)
  Removes the node’s children and marks the node as not loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnreferencenode/loadingpolicy)*