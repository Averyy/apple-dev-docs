# referenceURL

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The URL to a scene file from which to load content for the reference node.

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
var referenceURL: URL { get set }
```

```objc
@property (nonatomic, copy) NSURL * referenceURL;
```

#### Discussion

When the reference node loads its content (either automatically, according to the [`loadingPolicy`](./loadingpolicy.md) property, or when you call the [`load()`](./load%28%29.md) method), SceneKit loads the referenced scene file. All children of the scene file’s root node become children of the reference node.

## See Also

### Loading and Unloading a Reference Node’s Content
- [var loadingPolicy: SCNReferenceLoadingPolicy](./loadingpolicy.md)
  An option for whether to load the node’s content automatically.
- [func load()](./load%28%29.md)
  Loads content into the node from its referenced external scene file.
- [var isLoaded: Bool](./isloaded.md)
  A Boolean value that indicates whether the reference node has already loaded its content.
- [func unload()](./unload%28%29.md)
  Removes the node’s children and marks the node as not loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnreferencenode/referenceurl)*