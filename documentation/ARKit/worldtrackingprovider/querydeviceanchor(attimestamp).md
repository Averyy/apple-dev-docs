# queryDeviceAnchor(atTimestamp:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

The predicted pose of the current device at a given time.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
final func queryDeviceAnchor(atTimestamp timestamp: TimeInterval) -> DeviceAnchor?
```

## Return Value

The predicted position and orientation of the device at the time you specify.

## Discussion

Pass the `timestamp` parameter as absolute time in seconds. For example, to get the device’s current pose, pass [`CACurrentMediaTime()`](../../QuartzCore/cacurrentmediatime%28%29.md) as the timestamp.

> ❗ **Important**:  Predicting future device pose is a computationally expensive operation. You typically only use this method when implementing your own rendering with the [Compositor Services](../../CompositorServices/CompositorServices.md) framework.

## Parameters

- `timestamp`: A time — now or in the future — to predict the device pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/worldtrackingprovider/querydeviceanchor(attimestamp:))*