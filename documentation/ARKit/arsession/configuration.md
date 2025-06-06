# configuration

**Framework**: ARKit  
**Kind**: property

An object that defines motion and scene tracking behaviors for the session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@NSCopying
var configuration: ARConfiguration? { get }
```

## See Also

- [func run(ARConfiguration, options: ARSession.RunOptions)](arsession/run(_:options:).md)
  Starts AR processing for the session with the specified configuration and options.
- [var identifier: UUID](arsession/identifier.md)
  A unique identifier of the running session.
- [ARSession.RunOptions](arsession/runoptions.md)
  Options for transitioning an AR session’s current state when you change its configuration.
- [func pause()](arsession/pause.md)
  Pauses processing in the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/configuration)*