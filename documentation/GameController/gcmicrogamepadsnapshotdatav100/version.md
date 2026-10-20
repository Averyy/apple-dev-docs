# version

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

A value that indicates the version number of the data structure.

**Availability**:
- iOS 9.0+ - Deprecated in 13.0
- iPadOS 9.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.11+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`withMicroGamepad()`](../gccontroller/withmicrogamepad%28%29.md) method instead.

## Declaration

```swift
var version: UInt16
```

```c
uint16_t version;
```

#### Discussion

For the structure defined here, the Game Controller framework uses a value of `0x0100`.

## See Also

### Instance Properties
- [var buttonA: Float](./buttona.md)
  The value of the A button.
- [var buttonX: Float](./buttonx.md)
- [var dpadX: Float](./dpadx.md)
  The value of the horizontal axis of the dpad.
- [var dpadY: Float](./dpady.md)
  The value of the vertical axis of the dpad.
- [var size: UInt16](./size.md)
  The size of the recorded structure, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshotdatav100/version)*