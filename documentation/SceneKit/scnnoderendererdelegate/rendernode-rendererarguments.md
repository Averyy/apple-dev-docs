# renderNode(_:renderer:arguments:)

**Framework**: SceneKit  
**Kind**: method

Tells the delegate to perform rendering for a node.

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
optional func renderNode(_ node: SCNNode, renderer: SCNRenderer, arguments: [String : Any])
```

#### Discussion

Implement this method to perform custom rendering for a node. You should only execute Metal or OpenGL drawing commands (and any setup required to perform them) in this method—the results of modifying SceneKit objects in this method are undefined.

- To render using Metal, use the `renderer` parameter to retrieve the scene renderer’s [`currentRenderCommandEncoder`](scnscenerenderer/currentrendercommandencoder.md) object and encode your own drawing commands. If you need to reference other Metal state, see the properties listed in [`SCNSceneRenderer`](scnscenerenderer.md).
- To render using OpenGL, simply call the relevant OpenGL drawing commands—SceneKit automatically makes its OpenGL context the current context before calling this method. If you need to reference the OpenGL context being rendered into, examine the [`context`](scnscenerenderer/context.md) property of the `renderer` parameter.

You must draw using the appropriate graphics technology for the view currently being rendered. Use the [`renderingAPI`](scnscenerenderer/renderingapi.md) property of the `renderer` object to determine whether Metal or OpenGL is in use.

## Parameters

- `node`: The node to render.
- `renderer`: The SceneKit object (such as an   instance) responsible for rendering the scene.
- `arguments`: A dictionary containing transform information necessary for rendering the node. See Rendering Transform Keys for possible keys. The value for each key is an   object containing an   value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnoderendererdelegate/rendernode(_:renderer:arguments:))*