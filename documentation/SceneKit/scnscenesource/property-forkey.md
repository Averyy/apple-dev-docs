# property(forKey:)

**Framework**: SceneKit  
**Kind**: method

Returns metadata about the scene.

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
func property(forKey key: String) -> Any?
```

#### Return Value

The value for the metadata property, or `nil` if no value exists for the specified property.

#### Discussion

This method returns information about the scene that is defined in the file but is not directly referenced by the scene.

## Parameters

- `key`: A constant identifying a metadata property of the scene source. See   for available keys and the formats of their values.

## See Also

- [var url: URL?](scnscenesource/url.md)
  The URL identifying the file from which the scene source was created.
- [var data: Data?](scnscenesource/data.md)
  The data object from which the scene source loads scene content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource/property(forkey:))*