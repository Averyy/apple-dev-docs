# write(_:withSceneDocumentURL:originalImageURL:)

**Framework**: SceneKit  
**Kind**: method

Tells the delegate to export an image attached to a scene.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func write(_ image: NSImage, withSceneDocumentURL documentURL: URL, originalImageURL: URL?) -> URL?
```

#### Return Value

The URL your app exported the image to, or `nil` if your app did not write the image to a URL.

#### Discussion

If you implement this method, Scene Kit calls it for each image (for example, a texture) attached to the scene. Your app can then save the image data in a location and format of your choice, returning a URL for the exported image file.

If you do not provide a delegate when exporting a scene, or if your delegate returns `nil` from this method, Scene Kit exports the image in a default format to a default location.

## Parameters

- `image`: An image attached to the scene being exported.
- `documentURL`: The URL the scene is being exported to.
- `originalImageURL`: The URL the image was originally loaded from, or   if the image was not previously loaded from a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnsceneexportdelegate/write(_:withscenedocumenturl:originalimageurl:))*