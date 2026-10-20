# ARSession.RunOptions

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

Options for transitioning an AR session’s current state when you change its configuration.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
struct RunOptions
```

```c
enum ARSessionRunOptions : NSUInteger;
```

## Topics

### Creating Run Options
- [init(rawValue: UInt)](./runoptions/init%28rawvalue%29.md)
  Creates a run options.
### Run Options
- [static var resetTracking: ARSession.RunOptions](./runoptions/resettracking.md)
  An option to reset the device’s position from the session’s previous run.
- [static var removeExistingAnchors: ARSession.RunOptions](./runoptions/removeexistinganchors.md)
  An option to remove any anchor objects associated with the session’s previous run.
- [static var stopTrackedRaycasts: ARSession.RunOptions](./runoptions/stoptrackedraycasts.md)
  An option to stop all active tracked raycasts.
- [static var resetSceneReconstruction: ARSession.RunOptions](./runoptions/resetscenereconstruction.md)
  An option to reset the scene mesh.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Configuring and running a session
- [func run(ARConfiguration, options: ARSession.RunOptions)](./run%28_,options%29.md)
  Starts AR processing for the session with the specified configuration and options.
- [var identifier: UUID](./identifier.md)
  A unique identifier of the running session.
- [var configuration: ARConfiguration?](./configuration.md)
  An object that defines motion and scene tracking behaviors for the session.
- [func pause()](./pause%28%29.md)
  Pauses processing in the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/runoptions)*