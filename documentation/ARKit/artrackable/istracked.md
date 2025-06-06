# isTracked

**Framework**: ARKit  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the object’s transform is valid.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var isTracked: Bool { get }
```

#### Discussion

If this value is [`true`](https://developer.apple.com/documentation/swift/true), the object’s transform currently matches the position and orientation of the real-world object it represents.

If this value is [`false`](https://developer.apple.com/documentation/swift/false), the object is not guaranteed to match the movement of its corresponding real-world feature, even if it remains in the visible scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/artrackable/istracked)*