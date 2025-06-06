# ARSession.RunOptions

**Framework**: ARKit  
**Kind**: struct

Options for transitioning an AR session’s current state when you change its configuration.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
struct RunOptions
```

## Topics

### Creating Run Options
- [init(rawValue: UInt)](arsession/runoptions/init(rawvalue:).md)
  Creates a run options.
### Run Options
- [static var resetTracking: ARSession.RunOptions](arsession/runoptions/resettracking.md)
  An option to reset the device’s position from the session’s previous run.
- [static var removeExistingAnchors: ARSession.RunOptions](arsession/runoptions/removeexistinganchors.md)
  An option to remove any anchor objects associated with the session’s previous run.
- [static var stopTrackedRaycasts: ARSession.RunOptions](arsession/runoptions/stoptrackedraycasts.md)
  An option to stop all active tracked raycasts.
- [static var resetSceneReconstruction: ARSession.RunOptions](arsession/runoptions/resetscenereconstruction.md)
  An option to reset the scene mesh.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func run(ARConfiguration, options: ARSession.RunOptions)](arsession/run(_:options:).md)
  Starts AR processing for the session with the specified configuration and options.
- [var identifier: UUID](arsession/identifier.md)
  A unique identifier of the running session.
- [var configuration: ARConfiguration?](arsession/configuration.md)
  An object that defines motion and scene tracking behaviors for the session.
- [func pause()](arsession/pause.md)
  Pauses processing in the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/runoptions)*