# init()

**Framework**: ARKit  
**Kind**: init

Creates a new session.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
convenience init()
```

#### Discussion

ARKit stops sessions when they’re deinitialized.

## See Also

- [func run([any DataProvider]) async throws](arkitsession/run(_:).md)
  Runs a session with the data providers you supply.
- [func stop()](arkitsession/stop.md)
  Stops all data providers running in this session.
- [ARKitSession.Error](arkitsession/error.md)
  An error that might occur when running data providers on an ARKit session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/init())*