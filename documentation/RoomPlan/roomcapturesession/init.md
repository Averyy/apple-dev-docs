# init()

**Framework**: RoomPlan  
**Kind**: init

Creates a room-capture session with the given AR session.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS ?+

## Declaration

```swift
init()
```

#### Discussion

By providing your own [`ARSession`](https://developer.apple.com/documentation/ARKit/ARSession) object, you can continue your app’s existing AR experience by seamlessly transitioning into a room-scanning session with RoomPlan. In addition, continuing an `ARSession` across multiple room-capture sessions — specifically, different rooms in the same vicinity — enables you to merge multiple [`CapturedRoom`](capturedroom.md) objects into a single captured structure. For more information, see [`CapturedStructure`](capturedstructure.md).

You can access the AR session at runtime with the [`arSession`](roomcapturesession/arsession.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesession/init())*