# init(named:inDirectory:options:)

**Framework**: SceneKit  
**Kind**: init

Loads a scene from a file with the specified name in a specific subdirectory of the app’s main bundle.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
convenience init?(named name: String, inDirectory directory: String?, options: [SCNSceneSource.LoadingOption : Any]? = nil)
```

#### Return Value

A new scene object, or `nil` if no scene could be loaded.

#### Discussion

This method provides a convenient way to load a complete scene from a file in the app’s main bundle. Calling this method is equivalent to using the [`Bundle`](https://developer.apple.com/documentation/Foundation/Bundle) class to locate the scene file and passing the resulting URL to the [`init(url:options:)`](scnscene/init(url:options:).md) method.

For more detailed options or to load only part of a file’s scene graph, use the [`SCNSceneSource`](scnscenesource.md) class.

When creating a scene using Xcode’s Scene Editor or an external tool, you should copy your scene file into a directory with the .scnassets extension inside your app bundle. You should also place any image files referenced as textures from that scene in an Asset Catalog. Xcode will optimize the scene and texture resources for best performance on each target device, and prepare your texture resources for delivery features such as App Thinning and On-Demand Resources.

## Parameters

- `name`: The name of a scene file in the app bundle.
- `directory`: The path to the subdirectory of the bundle’s resources directory containing the scene file.
- `options`: A dictionary of options affecting scene loading, or   for default options. For available keys, see Scene Loading Options.

## See Also

- [convenience init?(named: String)](scnscene/init(named:).md)
  Loads a scene from a file with the specified name in the app’s main bundle.
- [convenience init(url: URL, options: [SCNSceneSource.LoadingOption : Any]?) throws](scnscene/init(url:options:).md)
  Loads a scene from the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/init(named:indirectory:options:))*