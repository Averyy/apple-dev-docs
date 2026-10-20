# canRequestImageCapture

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

Will be `true` only when a call to [`requestImageCapture()`](./requestimagecapture%28%29.md) is expected to be successful. It will be `false` when not in the `.capturing` state or if the session is too busy to currently process a new request. There is a period of time after requesting an image capture where this property will be `false` and a new call to [`requestImageCapture()`](./requestimagecapture%28%29.md)  will not produce a new image.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
@MainActor
var canRequestImageCapture: Bool { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/canrequestimagecapture)*