# init(updateMode:renderingMode:)

**Framework**: PHASE  
**Kind**: init

Creates a new engine that has both update and rendering modes.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
init(updateMode: PHASEEngine.UpdateMode, renderingMode: PHASEEngine.RenderingMode)
```

#### Discussion

In this initializer, the `updateMode` argument behaves the same as it does for [`init(updateMode:)`](phaseengine/init(updatemode:).md). The `renderingMode` parameter value you choose determines where the system renders audio.

An engine that you configure with [`PHASEEngine.RenderingMode.local`](phaseengine/renderingmode/local.md) renders audio locally, in process. Configuring an engine with [`PHASEEngine.RenderingMode.client`](phaseengine/renderingmode/client.md) renders audio remotely, in a secure rendering process.

## Parameters

- `updateMode`: An option that controls the timing of internal framework updates.
- `renderingMode`: Defines where the engine applies rendering. See   for more info.

## See Also

- [init(updateMode: PHASEEngine.UpdateMode)](phaseengine/init(updatemode:).md)
  Creates an engine updated by the app or framework.
- [PHASEEngine.UpdateMode](phaseengine/updatemode.md)
  Modes that determine when the framework consumes API calls and updates internal state.
- [PHASEEngine.RenderingMode](phaseengine/renderingmode.md)
  Modes that determine whether the system renders audio in process or out of process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseengine/init(updatemode:renderingmode:))*