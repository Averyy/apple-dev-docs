# data

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The data object from which the scene source loads scene content.

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
var data: Data? { get }
```

```objc
@property (readonly, nullable) NSData * data;
```

## Discussion

If the scene source was created using the [`sceneSourceWithData:options:`](./scenesourcewithdata_options_.md) or [`init(data:options:)`](./init%28data,options%29.md) method, this property’s value is the data from which the scene source was created. If the scene source was created from a scene file using the the [`sceneSourceWithURL:options:`](./scenesourcewithurl_options_.md) or [`init(url:options:)`](./init%28url,options%29-rw0y.md) method, this property’s value is the data loaded from that URL at the time the scene source was created.

## See Also

### Getting Information about the Scene
- [var url: URL?](./url.md)
  The URL identifying the file from which the scene source was created.
- [func property(forKey: String) -> Any?](./property%28forkey%29.md)
  Returns metadata about the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource/data)*