# next()

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Asynchronously advances to the next element and returns it, or ends the sequence if there’s no next element.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
mutating func next() async -> CameraFrameProvider.CameraFrameUpdates.Element?
```

## Return Value

The next element, if it exists, or nil to signal the end of the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameraframeprovider/cameraframeupdates/iterator/next())*