# sceneSourceWithData:options:

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates a scene source that reads the scene graph contained in an `NSData` object.

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
+ (instancetype) sceneSourceWithData:(NSData *) data options:(NSDictionary<NSString *,id> *) options;
```

#### Return Value

A new, initialized scene source object, or `nil` if initialization was not successful.

#### Discussion

The `data` parameter of this method (a [`NSData`](../../Foundation/nsdata.md)) should contain the same data as directly read from a scene file (such as by using the [`NSData`](../../Foundation/nsdata.md) method [`init(contentsOfURL:)`](../../Foundation/nsdata/init%28contentsofurl%29-5gfaw.md)). Use this method when you have the contents of a scene file but not the file itself—for example, if your app downloads scene files from the network.

## Parameters

- `data`: An data object containing a scene file in a format recognized by SceneKit.
- `options`: A dictionary containing options that affect scene loading. See `Scene Loading Options` for available keys and values. Pass `nil` to use default options.

## See Also

### Creating a Scene Source
- [+ sceneSourceWithURL:options:](./scenesourcewithurl_options_.md)
  Creates a scene source that reads the scene graph from a specified file.
- [init?(url: URL, options: [SCNSceneSource.LoadingOption : Any]?)](./init%28url,options%29-rw0y.md)
  Initializes a scene source for reading the scene graph from a specified file.
- [init?(data: Data, options: [SCNSceneSource.LoadingOption : Any]?)](./init%28data,options%29.md)
  Initializes a scene source for reading the scene graph contained in an `NSData` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource/scenesourcewithdata:options:)*