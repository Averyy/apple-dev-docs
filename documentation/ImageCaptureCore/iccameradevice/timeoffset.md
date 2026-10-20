# timeOffset

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

The time offset, in seconds, between the camera’s clock and the computer’s clock.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var timeOffset: TimeInterval { get }
```

```objc
@property (readonly) NSTimeInterval timeOffset;
```

#### Discussion

The value of this property is positive if the camera’s clock is ahead of the computer’s clock. Ignore this property if the camera’s [`capabilities`](../icdevice/capabilities.md) do not include [`cameraDeviceCanSyncClock`](../icdevicecapability/cameradevicecansyncclock.md).

## See Also

### Synchronizing the Clock
- [func requestSyncClock()](./requestsyncclock%28%29.md)
  Synchronizes the camera’s clock with the computer’s clock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevice/timeoffset)*