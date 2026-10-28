# SCNSceneExportProgressHandler

**Framework**: SceneKit  
**Kind**: typealias  
**Role**: Type Alias

The signature for the block that SceneKit calls during scene export.

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
typealias SCNSceneExportProgressHandler = (Float, (any Error)?, UnsafeMutablePointer<ObjCBool>) -> Void
```

```c
typedef void (^)(float, NSError *, _Bool *) SCNSceneExportProgressHandler;
```

## Discussion

You specify a block with this signature when calling the [`write(to:options:delegate:progressHandler:)`](./scnscene/write%28to,options,delegate,progresshandler%29.md) method in order to receive updates on the progress of the export operation. The block takes the following parameters:

- **totalProgress**: A number between `0.0` and `1.0` that indicates the progress of the export operation, with `0.0` indicating that the operation has just begun and `1.0` indicating the operation has completed.
- **error**: An error encountered during the export process, or `nil` if no errors have occurred.
- **stop**: Set `*stop` to [`true`](../Swift/true.md) inside the block to cancel export.

## See Also

### Constants
- [Scene Attributes](./scene-attributes.md)
  Attribute keys available in the options dictionary for the methods  [`attribute(forKey:)`](./scnscene/attribute%28forkey%29.md) and [`setAttribute(_:forKey:)`](./scnscene/setattribute%28_,forkey%29.md)
- [Scene Export Options](./scene-export-options.md)
  Options for the [`write(to:options:delegate:progressHandler:)`](./scnscene/write%28to,options,delegate,progresshandler%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnsceneexportprogresshandler)*