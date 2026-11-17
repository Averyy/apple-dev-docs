# next()

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Asynchronously retrieve the next camera frame.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
mutating func next() async -> CameraFrameProvider.CameraFrameUpdates.Element?
```

## Return Value

The next camera frame if one has been captured since the last call to this function. Otherwise suspends the caller until a new camera frame has been captured. Returns `nil` (signals end of the sequence) if the provider has been stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameraframeprovider/cameraframeupdates/iterator/next())*