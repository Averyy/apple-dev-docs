# isSupported

**Framework**: RealityKit  
**Kind**: property

A Boolean that indicates whether the current device supports object capture sessions.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
@MainActor
static var isSupported: Bool { get }
```

#### Discussion

Before creating an object capture session, check this value to make sure the current device supports the feature. If `false`, attempting to create an `ObjectCaptureSession` will result in a runtime error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/issupported)*