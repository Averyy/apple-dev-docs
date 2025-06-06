# init(name:transform:)

**Framework**: ARKit  
**Kind**: init

Creates a new anchor object with the specified transform and a descriptive name.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(name: String, transform: simd_float4x4)
```

#### Discussion

World coordinate space in ARKit always follows a right-handed convention, but is oriented based on the session configuration. For details, see [`Understanding World Tracking`](understanding-world-tracking.md).

#### Discussion

Use the [`add(anchor:)`](arsession/add(anchor:).md) method to begin tracking your custom anchor in an AR session.

## Parameters

- `name`: A descriptive name for the anchor. ARKit does not display the name to users, but your app can use it to identify anchors for debugging.
- `transform`: A matrix encoding the position, orientation, and scale of the anchor relative to the world coordinate space of the AR session the anchor is placed in.

## See Also

- [init(transform: simd_float4x4)](aranchor/init(transform:).md)
  Creates a new anchor object with the specified transform.
- [var name: String?](aranchor/name.md)
  A descriptive name for the anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/aranchor/init(name:transform:))*