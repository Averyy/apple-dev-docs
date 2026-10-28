# stop()

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Stops all data providers running in this session.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
final func stop()
```

## Discussion

ARKit also automatically stops sessions when they’re deinitialized.

## See Also

### Starting and stopping a session
- [convenience init()](./init%28%29.md)
  Creates a new session.
- [func run([any DataProvider]) async throws](./run%28_%29.md)
  Runs a session with the data providers you supply.
- [ARKitSession.Error](./error.md)
  An error that might occur when running data providers on an ARKit session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/stop())*