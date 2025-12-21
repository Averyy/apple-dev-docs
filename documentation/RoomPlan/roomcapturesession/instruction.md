# RoomCaptureSession.Instruction

**Framework**: RoomPlan  
**Kind**: enum

Instructions that the framework recommends the app display to the user.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS ?+

## Declaration

```swift
enum Instruction
```

## Mentions

- [Scanning the rooms of a single structure](scanning-the-rooms-of-a-single-structure.md)

#### Overview

Your app receives instructions through the [`captureSession(_:didProvide:)`](roomcapturesessiondelegate/capturesession(_:didprovide:).md) callback that the framework suggests you display to the user, such as by presenting the recommendation in a textual label.

## Topics

### Determining a coaching recommendation
- [RoomCaptureSession.Instruction.normal](roomcapturesession/instruction/normal.md)
  An instruction that indicates scanning proceeds normally and the user needs no coaching.
- [RoomCaptureSession.Instruction.moveCloseToWall](roomcapturesession/instruction/moveclosetowall.md)
  An instruction that requests the user move closer to the wall.
- [RoomCaptureSession.Instruction.moveAwayFromWall](roomcapturesession/instruction/moveawayfromwall.md)
  An instruction that requests the user move further from the wall.
- [RoomCaptureSession.Instruction.turnOnLight](roomcapturesession/instruction/turnonlight.md)
  An instruction that requests the user increase the amount of light in the room.
- [RoomCaptureSession.Instruction.slowDown](roomcapturesession/instruction/slowdown.md)
  An instruction that requests that the user move slower.
- [RoomCaptureSession.Instruction.lowTexture](roomcapturesession/instruction/lowtexture.md)
  An instruction that indicates the framework doesn’t detect distinguishable room features.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesession/instruction)*