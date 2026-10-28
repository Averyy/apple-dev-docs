# transform

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A matrix encoding the position, orientation, and scale of the anchor relative to the world coordinate space of the AR session the anchor is placed in.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
var transform: simd_float4x4 { get }
```

```objc
@property (nonatomic, readonly) simd_float4x4 transform;
```

## Mentions

- [Displaying an AR Experience with Metal](../displaying-an-ar-experience-with-metal.md)

## Discussion

World coordinate space in ARKit always follows a right-handed convention, but is oriented based on the session configuration. For details, see [Understanding World Tracking](../understanding-world-tracking.md).

## See Also

### Tracking Anchors
- [var identifier: UUID](./identifier.md)
  A unique identifier for the anchor.
- [var sessionIdentifier: UUID?](./sessionidentifier.md)
  The unique identifier of the session that owns this anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/aranchor/transform)*