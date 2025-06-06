# url

**Framework**: SceneKit  
**Kind**: property

The URL identifying the file from which the scene source was created.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var url: URL? { get }
```

#### Discussion

The value of this property is `nil` if the scene source was not created using the [`sceneSourceWithURL:options:`](scnscenesource/scenesourcewithurl:options:.md) or [`init(url:options:)`](scnscenesource/init(url:options:).md) method.

## See Also

- [var data: Data?](scnscenesource/data.md)
  The data object from which the scene source loads scene content.
- [func property(forKey: String) -> Any?](scnscenesource/property(forkey:).md)
  Returns metadata about the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource/url)*