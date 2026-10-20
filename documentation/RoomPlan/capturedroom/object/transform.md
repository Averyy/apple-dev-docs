# transform

**Framework**: RoomPlan  
**Kind**: property  
**Role**: Instance Property

A matrix that defines the object’s position and orientation in the room.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
var transform: simd_float4x4 { get }
```

## See Also

### Positioning and sizing an object
- [var dimensions: simd_float3](./dimensions.md)
  A bounding box sized to the object’s extremities.
- [var story: Int](./story.md)
  The floor number or level on which the object resides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/object/transform)*