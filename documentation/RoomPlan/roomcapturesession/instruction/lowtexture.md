# RoomCaptureSession.Instruction.lowTexture

**Framework**: RoomPlan  
**Kind**: case

An instruction that indicates the framework doesn’t detect distinguishable room features.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS ?+

## Declaration

```swift
case lowTexture
```

#### Discussion

The framework provides this instruction when:

- The user points the device at a wall with a solid color.
- The camera view finder doesn’t contain any wall edges or other defining shapes for the room.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesession/instruction/lowtexture)*