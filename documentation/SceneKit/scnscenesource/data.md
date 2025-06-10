# data

**Framework**: SceneKit  
**Kind**: property

The data object from which the scene source loads scene content.

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
var data: Data? { get }
```

#### Discussion

If the scene source was created using the [`sceneSourceWithData:options:`](scnscenesource/scenesourcewithdata:options:.md) or [`init(data:options:)`](scnscenesource/init(data:options:).md) method, this property’s value is the data from which the scene source was created. If the scene source was created from a scene file using the the [`sceneSourceWithURL:options:`](scnscenesource/scenesourcewithurl:options:.md) or [`init(url:options:)`](scnscenesource/init(url:options:).md) method, this property’s value is the data loaded from that URL at the time the scene source was created.

## See Also

- [var url: URL?](scnscenesource/url.md)
  The URL identifying the file from which the scene source was created.
- [func property(forKey: String) -> Any?](scnscenesource/property(forkey:).md)
  Returns metadata about the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource/data)*