# SCNSceneExportDelegate

**Framework**: SceneKit  
**Kind**: protocol  
**Role**: Protocol

Methods you can implement to participate in the process of exporting a scene to a file.

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
protocol SCNSceneExportDelegate : NSObjectProtocol
```

```objc
@protocol SCNSceneExportDelegate <NSObject>
```

#### Overview

When you call a [`SCNScene`](./scnscene.md) object’s [`write(to:options:delegate:progressHandler:)`](./scnscene/write%28to,options,delegate,progresshandler%29.md) method to export the scene’s content to a file, you can optionally specify a delegate object to receive these messages.

## Topics

### Writing Image Attachments
- [func write(UIImage, withSceneDocumentURL: URL, originalImageURL: URL?) -> URL?](./scnsceneexportdelegate/write%28_,withscenedocumenturl,originalimageurl%29.md)
  Tells the delegate to export an image attached to a scene.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Exporting a Scene File
- [func write(to: URL, options: [String : Any]?, delegate: (any SCNSceneExportDelegate)?, progressHandler: SCNSceneExportProgressHandler?) -> Bool](./scnscene/write%28to,options,delegate,progresshandler%29.md)
  Exports the scene and its contents to a file at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnsceneexportdelegate)*