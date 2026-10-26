# runWithConfiguration:

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Starts AR processing for the session with the specified configuration.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```objc
- (void) runWithConfiguration:(ARConfiguration *) configuration;
```

#### Discussion

The session tracks device motion, captures and processes scene imagery from the device camera, and coordinates with your [`delegate`](./delegate.md) object or [`ARSCNView`](../arscnview.md) or [`ARSKView`](../arskview.md) view only when running.

Calling this method on a session that has already started transitions immediately to the new session configuration. After you call this method, the session runs asynchronously.

To determine how existing session state transitions to the new configuration, use the [`run(_:options:)`](./run%28_,options%29.md) method instead. Calling [`runWithConfiguration:`](./runwithconfiguration_.md) is equivalent to calling [`run(_:options:)`](./run%28_,options%29.md) with no options enabled.

## Parameters

- `configuration`: An object that defines motion and scene tracking behaviors for the session.

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
- [func pause()](./pause%28%29.md)
  Pauses processing in the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/runwithconfiguration:)*