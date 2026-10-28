# init(transform:)

**Framework**: ARKit  
**Kind**: init  
**Role**: Initializer

Creates a new anchor object with the specified transform.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
init(transform: simd_float4x4)
```

```objc
- (instancetype) initWithTransform:(simd_float4x4) transform;
```

## Discussion

World coordinate space in ARKit always follows a right-handed convention, but is oriented based on the session configuration. For details, see [Understanding World Tracking](../understanding-world-tracking.md).

## Discussion

Use the [`add(anchor:)`](../arsession/add%28anchor%29.md) method to begin tracking your custom anchor in an AR session.

## Parameters

- `transform`: A matrix encoding the position, orientation, and scale of the anchor relative to the world coordinate space of the AR session the anchor is placed in.

## See Also

### Creating Anchors
- [init(name: String, transform: simd_float4x4)](./init%28name,transform%29.md)
  Creates a new anchor object with the specified transform and a descriptive name.
- [var name: String?](./name.md)
  A descriptive name for the anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/aranchor/init(transform:))*