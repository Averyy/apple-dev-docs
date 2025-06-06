# run(_:options:)

**Framework**: ARKit  
**Kind**: method

Starts AR processing for the session with the specified configuration and options.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func run(_ configuration: ARConfiguration, options: ARSession.RunOptions = [])
```

## Mentions

- [Managing Session Life Cycle and Tracking Quality](managing-session-life-cycle-and-tracking-quality.md)

#### Discussion

The session tracks device motion, captures and processes scene imagery from the device camera, and coordinates with your [`delegate`](arsession/delegate.md) object or [`ARSCNView`](arscnview.md) or [`ARSKView`](arskview.md) view only when running.

Calling this method on a session that has already started transitions immediately to the new session configuration. The `options` parameter determines how existing session state transitions to the new configuration. By default, the session resumes device position tracking from the last known state and keeps any anchors already included in the session (those you’ve added manually with [`add(anchor:)`](arsession/add(anchor:).md), as well as those added automatically by ARKit features such as plane detection or face tracking).

This method returns immediately when called, but the session continues to run.

## Parameters

- `configuration`: An object that defines motion and scene tracking behaviors for the session.
- `options`: If the session is running for the first time, this parameter has no effect.

## See Also

- [var identifier: UUID](arsession/identifier.md)
  A unique identifier of the running session.
- [ARSession.RunOptions](arsession/runoptions.md)
  Options for transitioning an AR session’s current state when you change its configuration.
- [var configuration: ARConfiguration?](arsession/configuration.md)
  An object that defines motion and scene tracking behaviors for the session.
- [func pause()](arsession/pause.md)
  Pauses processing in the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/run(_:options:))*