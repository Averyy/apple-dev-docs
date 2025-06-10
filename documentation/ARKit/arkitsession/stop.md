# stop()

**Framework**: ARKit  
**Kind**: method

Stops all data providers running in this session.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
final func stop()
```

#### Discussion

ARKit also automatically stops sessions when they’re deinitialized.

## See Also

- [convenience init()](arkitsession/init.md)
  Creates a new session.
- [func run([any DataProvider]) async throws](arkitsession/run(_:).md)
  Runs a session with the data providers you supply.
- [ARKitSession.Error](arkitsession/error.md)
  An error that might occur when running data providers on an ARKit session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/stop())*