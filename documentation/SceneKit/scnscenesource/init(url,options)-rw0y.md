# init(url:options:)

**Framework**: SceneKit  
**Kind**: init  
**Role**: Initializer

Initializes a scene source for reading the scene graph from a specified file.

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
init?(url: URL, options: [SCNSceneSource.LoadingOption : Any]? = nil)
```

```objc
- (instancetype) initWithURL:(NSURL *) url options:(NSDictionary<NSString *,id> *) options;
```

#### Return Value

An initialized scene source object, or `nil` if initialization was not successful.

#### Discussion

If you have the contents of a scene file but not the file itself (for example, if your app downloads scene files from the network), use the [`init(data:options:)`](./init%28data,options%29.md) method instead.

## Parameters

- `url`: The URL identifying the scene.
- `options`: A dictionary containing options that affect scene loading. See `Scene Loading Options` for available keys and values. Pass `nil` to use default options.

## See Also

### Creating a Scene Source
- [init?(data: Data, options: [SCNSceneSource.LoadingOption : Any]?)](./init%28data,options%29.md)
  Initializes a scene source for reading the scene graph contained in an `NSData` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource/init(url:options:)-rw0y)*