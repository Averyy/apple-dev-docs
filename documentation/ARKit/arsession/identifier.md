# identifier

**Framework**: ARKit  
**Kind**: property

A unique identifier of the running session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var identifier: UUID { get }
```

#### Discussion

This property might change after you call the run function, but not immediately. Therefore, to get the new value, listen for its change using key-value observation.

```swift
// Use key-value observation to monitor my ARSession's identifier.
var sessionIDObservation: NSKeyValueObservation?
...
sessionIDObservation = observe(
    .arView.session.identifier,
    options: [.old, .new]) { 
        object, change in
        print("SessionID changed to: \(change.newValue!)")
    }
```

## See Also

- [func run(ARConfiguration, options: ARSession.RunOptions)](arsession/run(_:options:).md)
  Starts AR processing for the session with the specified configuration and options.
- [ARSession.RunOptions](arsession/runoptions.md)
  Options for transitioning an AR session’s current state when you change its configuration.
- [var configuration: ARConfiguration?](arsession/configuration.md)
  An object that defines motion and scene tracking behaviors for the session.
- [func pause()](arsession/pause.md)
  Pauses processing in the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/identifier)*