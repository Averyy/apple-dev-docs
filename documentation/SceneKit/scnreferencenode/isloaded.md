# isLoaded

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the reference node has already loaded its content.

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
var isLoaded: Bool { get }
```

```objc
@property (readonly, getter=isLoaded) BOOL loaded;
```

## See Also

### Loading and Unloading a Reference Node’s Content
- [var referenceURL: URL](./referenceurl.md)
  The URL to a scene file from which to load content for the reference node.
- [var loadingPolicy: SCNReferenceLoadingPolicy](./loadingpolicy.md)
  An option for whether to load the node’s content automatically.
- [func load()](./load%28%29.md)
  Loads content into the node from its referenced external scene file.
- [func unload()](./unload%28%29.md)
  Removes the node’s children and marks the node as not loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnreferencenode/isloaded)*