# pause()

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Pauses processing in the session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
func pause()
```

```objc
- (void) pause;
```

## Discussion

While paused, the session doesn’t track device motion or capture scene imagery, nor does it coordinate with its [`delegate`](./delegate.md) object or update any associated [`RealityView`](../../RealityKit/realityview.md) or [`ARView`](../../RealityKit/arview.md) object.

## See Also

### Configuring and running a session
- [func run(ARConfiguration, options: ARSession.RunOptions)](./run%28_,options%29.md)
  Starts AR processing for the session with the specified configuration and options.
- [var identifier: UUID](./identifier.md)
  A unique identifier of the running session.
- [ARSession.RunOptions](./runoptions.md)
  Options for transitioning an AR session’s current state when you change its configuration.
- [var configuration: ARConfiguration?](./configuration.md)
  An object that defines motion and scene tracking behaviors for the session.
- [- runWithConfiguration:](./runwithconfiguration_.md)
  Starts AR processing for the session with the specified configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/pause())*