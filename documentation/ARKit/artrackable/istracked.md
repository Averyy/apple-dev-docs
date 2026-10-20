# isTracked

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates whether the object’s transform is valid.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
var isTracked: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isTracked;
```

#### Discussion

If this value is [`true`](../../Swift/true.md), the object’s transform currently matches the position and orientation of the real-world object it represents.

If this value is [`false`](../../Swift/false.md), the object is not guaranteed to match the movement of its corresponding real-world feature, even if it remains in the visible scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/artrackable/istracked)*