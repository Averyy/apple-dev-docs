# SCNSceneExportDelegate

**Framework**: SceneKit  
**Kind**: protocol

Methods you can implement to participate in the process of exporting a scene to a file.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
protocol SCNSceneExportDelegate : NSObjectProtocol
```

#### Overview

When you call a [`SCNScene`](scnscene.md) object’s [`write(to:options:delegate:progressHandler:)`](scnscene/write(to:options:delegate:progresshandler:).md) method to export the scene’s content to a file, you can optionally specify a delegate object to receive these messages.

## Topics

### Writing Image Attachments
- [func write(UIImage, withSceneDocumentURL: URL, originalImageURL: URL?) -> URL?](scnsceneexportdelegate/write(_:withscenedocumenturl:originalimageurl:).md)
  Tells the delegate to export an image attached to a scene.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func write(to: URL, options: [String : Any]?, delegate: (any SCNSceneExportDelegate)?, progressHandler: SCNSceneExportProgressHandler?) -> Bool](scnscene/write(to:options:delegate:progresshandler:).md)
  Exports the scene and its contents to a file at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnsceneexportdelegate)*