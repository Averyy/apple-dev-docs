# acquireDevice()

**Framework**: Game Controller  
**Kind**: method

Starts receiving events from the racing wheel.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
func acquireDevice() throws
```

#### Discussion

Before invoking this method, the racing wheel doesn’t deliver events to your app. Since only one app may receive racing wheel events at a time, this method can fail to acquire the device.

## See Also

- [func relinquishDevice()](gcracingwheel/relinquishdevice.md)
  Stops receiving events from the racing wheel.
- [var isAcquired: Bool](gcracingwheel/isacquired.md)
  A Boolean value that indicates whether the racing wheel sends events to the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcracingwheel/acquiredevice())*