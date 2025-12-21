# init(url:)

**Framework**: SceneKit  
**Kind**: init

Initializes a node whose content is to be loaded from the referenced URL.

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
init?(url referenceURL: URL)
```

#### Return Value

A new reference node.

#### Discussion

Using this initializer does not load the node’s content. To load content from the referenced URL, use the [`load()`](scnreferencenode/load().md) method.

## Parameters

- `referenceURL`: The URL to a scene file from which to load the node’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnreferencenode/init(url:))*