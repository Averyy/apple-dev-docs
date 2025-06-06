# requestSyncClock()

**Framework**: ImageCaptureCore  
**Kind**: method

Synchronizes the camera’s clock with the computer’s clock.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func requestSyncClock()
```

#### Discussion

Send this request only if the camera has the [`cameraDeviceCanSyncClock`](icdevicecapability/cameradevicecansyncclock.md) capability.

## See Also

- [var timeOffset: TimeInterval](iccameradevice/timeoffset.md)
  The time offset, in seconds, between the camera’s clock and the computer’s clock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevice/requestsyncclock())*