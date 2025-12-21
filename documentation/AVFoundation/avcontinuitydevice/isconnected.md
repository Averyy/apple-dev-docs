# isConnected

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether you can use the continuity device because it’s connected to the system.

**Availability**:
- tvOS 17.0+

## Declaration

```swift
var isConnected: Bool { get }
```

#### Discussion

The value of the property can change from [`true`](https://developer.apple.com/documentation/Swift/true) to [`false`](https://developer.apple.com/documentation/Swift/false), but not the reverse. Instead, the system creates a new [`AVContinuityDevice`](avcontinuitydevice.md) instance when the same physical device reconnects to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontinuitydevice/isconnected)*