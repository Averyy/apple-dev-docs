# identifier

**Framework**: ARKit  
**Kind**: property

A unique identifier for the anchor.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var identifier: UUID { get }
```

#### Discussion

Whether an anchor is created manually (with the [`init(transform:)`](aranchor/init(transform:).md) initializer) or automatically by ARKit (and provided to you through [`ARSessionDelegate`](arsessiondelegate.md), [`ARSCNViewDelegate`](arscnviewdelegate.md), or [`ARSKViewDelegate`](arskviewdelegate.md) methods), each anchor automatically receives a unique identifier value.

You can use this value to determine which anchors accompanying a specific [`ARFrame`](arframe.md) capture correspond to anchors in frames captured previously.

## See Also

- [var sessionIdentifier: UUID?](aranchor/sessionidentifier.md)
  The unique identifier of the session that owns this anchor.
- [var transform: simd_float4x4](aranchor/transform.md)
  A matrix encoding the position, orientation, and scale of the anchor relative to the world coordinate space of the AR session the anchor is placed in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/aranchor/identifier)*