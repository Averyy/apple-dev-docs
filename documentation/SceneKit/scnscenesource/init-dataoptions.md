# init(data:options:)

**Framework**: SceneKit  
**Kind**: init

Initializes a scene source for reading the scene graph contained in an `NSData` object.

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
init?(data: Data, options: [SCNSceneSource.LoadingOption : Any]? = nil)
```

#### Return Value

An initialized scene source object, or `nil` if initialization was not successful.

#### Discussion

The `data` parameter of this method (an [`NSData`](https://developer.apple.com/documentation/Foundation/NSData)) should contain the same data as directly read from a scene file (such as by using the [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) method [`init(contentsOfURL:)`](https://developer.apple.com/documentation/Foundation/NSData/init(contentsOfURL:)-6foqd)). Use this method when you have the contents of a scene file but not the file itself—for example, if your app downloads scene files from the network.

## Parameters

- `data`: A data object containing a scene file in a format recognized by SceneKit.
- `options`: A dictionary containing options that affect scene loading. See   for available keys and values. Pass   to use default options.

## See Also

- [init?(url: URL, options: [SCNSceneSource.LoadingOption : Any]?)](scnscenesource/init(url:options:).md)
  Initializes a scene source for reading the scene graph from a specified file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenesource/init(data:options:))*