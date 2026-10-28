# referenceNodeWithURL:

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates a node whose content is to be loaded from the referenced URL.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```objc
+ (instancetype) referenceNodeWithURL:(NSURL *) referenceURL;
```

## Return Value

A new reference node.

## Discussion

Using this method does not load the node’s content. To load content from the referenced URL, use the [`load()`](./load%28%29.md) method.

## Parameters

- `referenceURL`: The URL to a scene file from which to load the node’s content.

## See Also

### Creating a Reference Node
- [init?(url: URL)](./init%28url%29-9dkfj.md)
  Initializes a node whose content is to be loaded from the referenced URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnreferencenode/referencenodewithurl:)*