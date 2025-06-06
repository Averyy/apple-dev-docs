# configuration

**Framework**: RealityKit  
**Kind**: property

The read-only `Configuration` used to start the capture session.  The configuration can be set by passing it to the `start()` call and it remains immutable after the session is started successfully.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
@MainActor
var configuration: ObjectCaptureSession.Configuration { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/configuration-swift.property)*