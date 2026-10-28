# loadingPolicy

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

An option for whether to load the node’s content automatically.

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
var loadingPolicy: SCNReferenceLoadingPolicy { get set }
```

```objc
@property (nonatomic) SCNReferenceLoadingPolicy loadingPolicy;
```

## Discussion

If this property’s value is [`SCNReferenceLoadingPolicy.immediate`](../scnreferenceloadingpolicy/immediate.md) (the default), instantiating a reference node from an archive (using the [`NSKeyedUnarchiver`](../../Foundation/nskeyedunarchiver.md) class) automatically loads the node’s external content. Set this property to [`SCNReferenceLoadingPolicy.onDemand`](../scnreferenceloadingpolicy/ondemand.md) before archiving an [`SCNReferenceNode`](../scnreferencenode.md) object if you don’t want that reference node to automatically load its content when unarchived. In that case, call the [`load()`](./load%28%29.md) method after unarchiving when you want to load the node’s content.

## See Also

### Loading and Unloading a Reference Node’s Content
- [var referenceURL: URL](./referenceurl.md)
  The URL to a scene file from which to load content for the reference node.
- [func load()](./load%28%29.md)
  Loads content into the node from its referenced external scene file.
- [var isLoaded: Bool](./isloaded.md)
  A Boolean value that indicates whether the reference node has already loaded its content.
- [func unload()](./unload%28%29.md)
  Removes the node’s children and marks the node as not loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnreferencenode/loadingpolicy)*