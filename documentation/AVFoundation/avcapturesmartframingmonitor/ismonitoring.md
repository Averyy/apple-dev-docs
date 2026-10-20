# isMonitoring

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Yes when the receiver is actively monitoring.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var isMonitoring: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isMonitoring) BOOL monitoring;
```

#### Discussion

See [`startMonitoring()`](./startmonitoring%28%29.md) and [`stopMonitoring()`](./stopmonitoring%28%29.md).

## See Also

### Managing the life cycle
- [func startMonitoring() throws](./startmonitoring%28%29.md)
  Begins monitoring the device’s active scene and making framing recommendations.
- [func stopMonitoring()](./stopmonitoring%28%29.md)
  Stops monitoring the device’s active scene and making framing recommendations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesmartframingmonitor/ismonitoring)*