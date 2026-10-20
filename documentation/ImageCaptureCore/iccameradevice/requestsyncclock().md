# requestSyncClock()

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Synchronizes the camera’s clock with the computer’s clock.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func requestSyncClock()
```

```objc
- (void) requestSyncClock;
```

#### Discussion

Send this request only if the camera has the [`cameraDeviceCanSyncClock`](../icdevicecapability/cameradevicecansyncclock.md) capability.

## See Also

### Synchronizing the Clock
- [var timeOffset: TimeInterval](./timeoffset.md)
  The time offset, in seconds, between the camera’s clock and the computer’s clock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevice/requestsyncclock())*