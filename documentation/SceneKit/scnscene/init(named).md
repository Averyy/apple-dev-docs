# init(named:)

**Framework**: SceneKit  
**Kind**: init  
**Role**: Initializer

Loads a scene from a file with the specified name in the app’s main bundle.

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
convenience init?(named name: String)
```

```objc
+ (instancetype) sceneNamed:(NSString *) name;
```

## Return Value

A new scene object, or `nil` if no scene could be loaded.

## Discussion

This method provides a convenient way to load a complete scene from a file in the app’s main bundle. Calling this method is equivalent to using the [`Bundle`](../../Foundation/bundle.md) class to locate the scene file and passing the resulting URL to the [`init(url:options:)`](./init%28url,options%29-7ugvv.md) method, specifying no options and no error handling.

For more detailed options or to load only part of a file’s scene graph, use the [`SCNSceneSource`](../scnscenesource.md) class.

When creating a scene using Xcode’s Scene Editor or an external tool, you should copy your scene file into a directory with the .scnassets extension inside your app bundle. You should also place any image files referenced as textures from that scene in an Asset Catalog. Xcode will optimize the scene and texture resources for best performance on each target device, and prepare your texture resources for delivery features such as App Thinning and On-Demand Resources.

## Parameters

- `name`: The name of a scene file in the app bundle’s resources directory.

## See Also

### Creating a Scene from a File
- [convenience init?(named: String, inDirectory: String?, options: [SCNSceneSource.LoadingOption : Any]?)](./init%28named,indirectory,options%29.md)
  Loads a scene from a file with the specified name in a specific subdirectory of the app’s main bundle.
- [convenience init(url: URL, options: [SCNSceneSource.LoadingOption : Any]?) throws](./init%28url,options%29-7ugvv.md)
  Loads a scene from the specified URL.
- [+ scene](./scene.md)
  Creates and returns an empty scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/init(named:))*