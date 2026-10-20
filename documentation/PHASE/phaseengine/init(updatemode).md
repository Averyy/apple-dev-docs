# init(updateMode:)

**Framework**: PHASE  
**Kind**: init  
**Role**: Initializer

Creates an engine updated by the app or framework.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(updateMode: PHASEEngine.UpdateMode)
```

```objc
- (instancetype) initWithUpdateMode:(PHASEUpdateMode) updateMode;
```

#### Discussion

The argument you choose determines the rate at which the engine consumes user commands, performs internal updates, and executes callbacks.

When an app calls a PHASE function, the framework defers processing the call until the next update. An engine you configure with [`PHASEEngine.UpdateMode.manual`](./updatemode/manual.md) controls when the framework processes those calls. For example, an app can ensure that two sound events begin simultaneously by following their creation with an [`update()`](./update%28%29.md). Apps that don’t require advanced call synchronization select [`PHASEEngine.UpdateMode.automatic`](./updatemode/automatic.md).

## Parameters

- `updateMode`: An option that controls the timing of internal framework updates.

## See Also

### Creating an Engine
- [init(updateMode: PHASEEngine.UpdateMode, renderingMode: PHASEEngine.RenderingMode)](./init%28updatemode,renderingmode%29.md)
  Creates a new engine that has both update and rendering modes.
- [PHASEEngine.UpdateMode](./updatemode.md)
  Modes that determine when the framework consumes API calls and updates internal state.
- [PHASEEngine.RenderingMode](./renderingmode.md)
  Modes that determine whether the system renders audio in process or out of process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseengine/init(updatemode:))*