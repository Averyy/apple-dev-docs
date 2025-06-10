# penetrationDistance

**Framework**: RealityKit  
**Kind**: property

The estimated distance of overlap between the two colliding entities in scene coordinate space.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
var penetrationDistance: Float { get }
```

#### Discussion

This is the maximum penetration distance for all contacts, for more detailed penetration distance see `contacts` and `CollisionComponent/CollisionOptions-swift.struct/fullContactInformation`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisionevents/began/penetrationdistance-5stle)*