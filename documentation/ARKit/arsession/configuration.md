# configuration

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

An object that defines motion and scene tracking behaviors for the session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
@NSCopying
var configuration: ARConfiguration? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) ARConfiguration * configuration;
```

## See Also

### Configuring and running a session
- [func run(ARConfiguration, options: ARSession.RunOptions)](./run%28_,options%29.md)
  Starts AR processing for the session with the specified configuration and options.
- [var identifier: UUID](./identifier.md)
  A unique identifier of the running session.
- [ARSession.RunOptions](./runoptions.md)
  Options for transitioning an AR session’s current state when you change its configuration.
- [func pause()](./pause%28%29.md)
  Pauses processing in the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/configuration)*