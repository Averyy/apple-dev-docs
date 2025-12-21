# pause()

**Framework**: ARKit  
**Kind**: method

Pauses processing in the session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func pause()
```

#### Discussion

While paused, the session doesn’t track device motion or capture scene imagery, nor does it coordinate with its [`delegate`](arsession/delegate.md) object or update any associated [`RealityView`](https://developer.apple.com/documentation/RealityKit/RealityView) or [`ARView`](https://developer.apple.com/documentation/RealityKit/ARView) object.

## See Also

- [func run(ARConfiguration, options: ARSession.RunOptions)](arsession/run(_:options:).md)
  Starts AR processing for the session with the specified configuration and options.
- [var identifier: UUID](arsession/identifier.md)
  A unique identifier of the running session.
- [ARSession.RunOptions](arsession/runoptions.md)
  Options for transitioning an AR session’s current state when you change its configuration.
- [var configuration: ARConfiguration?](arsession/configuration.md)
  An object that defines motion and scene tracking behaviors for the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/pause())*