# url

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The URL identifying the file from which the scene source was created.

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
var url: URL? { get }
```

```objc
@property (readonly, nullable) NSURL * url;
```

## Discussion

The value of this property is `nil` if the scene source was not created using the [`sceneSourceWithURL:options:`](./scenesourcewithurl_options_.md) or [`init(url:options:)`](./init%28url,options%29-rw0y.md) method.

## See Also

### Getting Information about the Scene
- [var data: Data?](./data.md)
  The data object from which the scene source loads scene content.
- [func property(forKey: String) -> Any?](./property%28forkey%29.md)
  Returns metadata about the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource/url)*