# init(url:options:)

**Framework**: SceneKit  
**Kind**: init

Initializes a scene source for reading the scene graph from a specified file.

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
init?(url: URL, options: [SCNSceneSource.LoadingOption : Any]? = nil)
```

#### Return Value

An initialized scene source object, or `nil` if initialization was not successful.

#### Discussion

If you have the contents of a scene file but not the file itself (for example, if your app downloads scene files from the network), use the [`init(data:options:)`](scnscenesource/init(data:options:).md) method instead.

## Parameters

- `url`: The URL identifying the scene.
- `options`: A dictionary containing options that affect scene loading. See   for available keys and values. Pass   to use default options.

## See Also

- [init?(data: Data, options: [SCNSceneSource.LoadingOption : Any]?)](scnscenesource/init(data:options:).md)
  Initializes a scene source for reading the scene graph contained in an `NSData` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource/init(url:options:))*