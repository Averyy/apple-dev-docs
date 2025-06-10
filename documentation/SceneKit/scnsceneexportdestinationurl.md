# SCNSceneExportDestinationURL

**Framework**: SceneKit  
**Kind**: var

The final destination `URL` for the exported scene file.

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
let SCNSceneExportDestinationURL: String
```

#### Discussion

Use this option if you export a scene to a temporary directory and then move it to a final location. You must specify a final destination URL (an [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) object) if your scene references external resources, such as image files for textures. SceneKit uses this URL to construct appropriate paths for external resources when writing the scene file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnsceneexportdestinationurl)*