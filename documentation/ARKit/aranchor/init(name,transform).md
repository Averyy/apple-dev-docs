# init(name:transform:)

**Framework**: ARKit  
**Kind**: init  
**Role**: Initializer

Creates a new anchor object with the specified transform and a descriptive name.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
init(name: String, transform: simd_float4x4)
```

```objc
- (instancetype) initWithName:(NSString *) name transform:(simd_float4x4) transform;
```

## Discussion

World coordinate space in ARKit always follows a right-handed convention, but is oriented based on the session configuration. For details, see [Understanding World Tracking](../understanding-world-tracking.md).

## Discussion

Use the [`add(anchor:)`](../arsession/add%28anchor%29.md) method to begin tracking your custom anchor in an AR session.

## Parameters

- `name`: A descriptive name for the anchor. ARKit does not display the name to users, but your app can use it to identify anchors for debugging.
- `transform`: A matrix encoding the position, orientation, and scale of the anchor relative to the world coordinate space of the AR session the anchor is placed in.

## See Also

### Creating Anchors
- [init(transform: simd_float4x4)](./init%28transform%29.md)
  Creates a new anchor object with the specified transform.
- [var name: String?](./name.md)
  A descriptive name for the anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/aranchor/init(name:transform:))*