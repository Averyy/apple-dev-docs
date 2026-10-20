# init(updateMode:renderingMode:)

**Framework**: PHASE  
**Kind**: init  
**Role**: Initializer

Creates a new engine that has both update and rendering modes.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
init(updateMode: PHASEEngine.UpdateMode, renderingMode: PHASEEngine.RenderingMode)
```

```objc
- (instancetype) initWithUpdateMode:(PHASEUpdateMode) updateMode renderingMode:(PHASERenderingMode) renderingMode;
```

#### Discussion

In this initializer, the `updateMode` argument behaves the same as it does for [`init(updateMode:)`](./init%28updatemode%29.md). The `renderingMode` parameter value you choose determines where the system renders audio.

An engine that you configure with [`PHASEEngine.RenderingMode.local`](./renderingmode/local.md) renders audio locally, in process. Configuring an engine with [`PHASEEngine.RenderingMode.client`](./renderingmode/client.md) renders audio remotely, in a secure rendering process.

## Parameters

- `updateMode`: An option that controls the timing of internal framework updates.
- `renderingMode`: Defines where the engine applies rendering. See [`PHASEEngine.RenderingMode`](./renderingmode.md) for more info.

## See Also

### Creating an Engine
- [init(updateMode: PHASEEngine.UpdateMode)](./init%28updatemode%29.md)
  Creates an engine updated by the app or framework.
- [PHASEEngine.UpdateMode](./updatemode.md)
  Modes that determine when the framework consumes API calls and updates internal state.
- [PHASEEngine.RenderingMode](./renderingmode.md)
  Modes that determine whether the system renders audio in process or out of process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseengine/init(updatemode:renderingmode:))*