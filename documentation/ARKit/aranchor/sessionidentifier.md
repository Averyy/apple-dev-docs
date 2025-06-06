# sessionIdentifier

**Framework**: ARKit  
**Kind**: property

The unique identifier of the session that owns this anchor.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var sessionIdentifier: UUID? { get }
```

#### Discussion

ARKit sets this property when a user first adds an anchor to a session. In multiuser experiences, use this ID to identify the user that created the anchor.

## See Also

- [var identifier: UUID](aranchor/identifier.md)
  A unique identifier for the anchor.
- [var transform: simd_float4x4](aranchor/transform.md)
  A matrix encoding the position, orientation, and scale of the anchor relative to the world coordinate space of the AR session the anchor is placed in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/aranchor/sessionidentifier)*