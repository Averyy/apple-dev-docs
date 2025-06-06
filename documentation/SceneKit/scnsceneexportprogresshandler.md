# SCNSceneExportProgressHandler

**Framework**: SceneKit  
**Kind**: typealias

The signature for the block that SceneKit calls during scene export.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias SCNSceneExportProgressHandler = (Float, (any Error)?, UnsafeMutablePointer<ObjCBool>) -> Void
```

#### Discussion

You specify a block with this signature when calling the [`write(to:options:delegate:progressHandler:)`](scnscene/write(to:options:delegate:progresshandler:).md) method in order to receive updates on the progress of the export operation. The block takes the following parameters:

## See Also

- [Scene Attributes](scene-attributes.md)
  Attribute keys available in the options dictionary for the methods  [`attribute(forKey:)`](scnscene/attribute(forkey:).md) and [`setAttribute(_:forKey:)`](scnscene/setattribute(_:forkey:).md)
- [Scene Export Options](scene-export-options.md)
  Options for the [`write(to:options:delegate:progressHandler:)`](scnscene/write(to:options:delegate:progresshandler:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnsceneexportprogresshandler)*