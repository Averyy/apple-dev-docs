# unload()

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Removes the node’s children and marks the node as not loaded.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
func unload()
```

```objc
- (void) unload;
```

#### Discussion

Calling this method does not necessarily unload any content associated with the node’s child nodes from memory—it merely removes them from the scene graph. The unlinked nodes and their content are then subject to normal object memory management rules. Under ARC, those objects are deallocated if and only if they are not referenced from elsewhere in your program.

## See Also

### Loading and Unloading a Reference Node’s Content
- [var referenceURL: URL](./referenceurl.md)
  The URL to a scene file from which to load content for the reference node.
- [var loadingPolicy: SCNReferenceLoadingPolicy](./loadingpolicy.md)
  An option for whether to load the node’s content automatically.
- [func load()](./load%28%29.md)
  Loads content into the node from its referenced external scene file.
- [var isLoaded: Bool](./isloaded.md)
  A Boolean value that indicates whether the reference node has already loaded its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnreferencenode/unload())*