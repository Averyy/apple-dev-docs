# name

**Framework**: SceneKit  
**Kind**: property

A name associated with the material.

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
var name: String? { get set }
```

#### Discussion

You can provide a descriptive name for a material to make managing your scene graph easier. Materials loaded from a scene file may have names assigned by an artist using a 3D authoring tool. Use the [`SCNSceneSource`](scnscenesource.md) class to examine materials in a scene file without loading its scene graph.

Material names are saved when you export a scene to a file using its [`write(to:options:delegate:progressHandler:)`](scnscene/write(to:options:delegate:progresshandler:).md) method, and appear in the Xcode scene editor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/name)*