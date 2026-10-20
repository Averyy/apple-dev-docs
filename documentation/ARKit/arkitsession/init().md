# init()

**Framework**: ARKit  
**Kind**: init  
**Role**: Initializer

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

### Starting and stopping a session
- [func run([any DataProvider]) async throws](./run%28_%29.md)
  Runs a session with the data providers you supply.
- [func stop()](./stop%28%29.md)
  Stops all data providers running in this session.
- [ARKitSession.Error](./error.md)
  An error that might occur when running data providers on an ARKit session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/init())*