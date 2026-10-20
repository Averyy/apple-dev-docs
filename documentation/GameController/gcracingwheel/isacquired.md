# isAcquired

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the racing wheel sends events to the app.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
var isAcquired: Bool { get }
```

```objc
@property (readonly, getter=isAcquired) BOOL acquired;
```

## See Also

### Getting events
- [func acquireDevice() throws](./acquiredevice%28%29.md)
  Starts receiving events from the racing wheel.
- [func relinquishDevice()](./relinquishdevice%28%29.md)
  Stops receiving events from the racing wheel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcracingwheel/isacquired)*