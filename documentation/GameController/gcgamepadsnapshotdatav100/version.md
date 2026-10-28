# version

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

A value that indicates the version number of the data structure.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0
- iPadOS 7.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`GCExtendedGamepad`](../gcextendedgamepad.md) class instead.

## Declaration

```swift
var version: UInt16
```

```c
uint16_t version;
```

## Discussion

For the structure defined here, the Game Controller framework uses a value of `0x0100`.

## See Also

### Instance Properties
- [var buttonA: Float](./buttona.md)
  The value of the A button.
- [var buttonB: Float](./buttonb.md)
  The value of the B button.
- [var buttonX: Float](./buttonx.md)
  The value of the X button.
- [var buttonY: Float](./buttony.md)
  The value of the Y button.
- [var dpadX: Float](./dpadx.md)
  The value of the horizontal axis of the dpad.
- [var dpadY: Float](./dpady.md)
  The value of the vertical axis of the dpad.
- [var leftShoulder: Float](./leftshoulder.md)
  The value of the left shoulder button.
- [var rightShoulder: Float](./rightshoulder.md)
  The value of the right shoulder button.
- [var size: UInt16](./size.md)
  The size of the recorded structure, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshotdatav100/version)*