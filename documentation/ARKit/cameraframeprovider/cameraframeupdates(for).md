# cameraFrameUpdates(for:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Gets a sequence of camera frame updates for a given video format.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
final func cameraFrameUpdates(for cameraVideoFormat: CameraVideoFormat) -> CameraFrameProvider.CameraFrameUpdates?
```

## Return Value

The sequence of camera frame updates. Returns `nil` if the provider wasn’t initialized with this format.

## Parameters

- `cameraVideoFormat`: The camera video format to get updates for.

## See Also

### Getting camera frame updates
- [CameraFrameProvider.CameraFrameUpdates](./cameraframeupdates.md)
  A sequence of camera frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameraframeprovider/cameraframeupdates(for:))*