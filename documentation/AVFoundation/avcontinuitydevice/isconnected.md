# isConnected

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether you can use the continuity device because it’s connected to the system.

**Availability**:
- tvOS 17.0+

## Declaration

```swift
var isConnected: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isConnected) BOOL connected;
```

## Discussion

The value of the property can change from [`true`](../../Swift/true.md) to [`false`](../../Swift/false.md), but not the reverse. Instead, the system creates a new [`AVContinuityDevice`](../avcontinuitydevice.md) instance when the same physical device reconnects to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontinuitydevice/isconnected)*