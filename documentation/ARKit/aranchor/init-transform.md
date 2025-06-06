# init(transform:)

**Framework**: ARKit  
**Kind**: init

Creates a new anchor object with the specified transform.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(transform: simd_float4x4)
```

#### Discussion

World coordinate space in ARKit always follows a right-handed convention, but is oriented based on the session configuration. For details, see [`Understanding World Tracking`](understanding-world-tracking.md).

#### Discussion

Use the [`add(anchor:)`](arsession/add(anchor:).md) method to begin tracking your custom anchor in an AR session.

## Parameters

- `transform`: A matrix encoding the position, orientation, and scale of the anchor relative to the world coordinate space of the AR session the anchor is placed in.

## See Also

- [init(name: String, transform: simd_float4x4)](aranchor/init(name:transform:).md)
  Creates a new anchor object with the specified transform and a descriptive name.
- [var name: String?](aranchor/name.md)
  A descriptive name for the anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/aranchor/init(transform:))*