# armPosition

**Framework**: Game Controller  
**Kind**: property

The position of the trigger’s arm.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
var armPosition: Float { get }
```

#### Discussion

This property represents the value of the stepped mechanical arm inside the trigger and isn’t the same as the trigger’s inherited `value` property. This property ranges between `0` and `1`, where `0` represents the minimum and `1` represents the maximum position.

## See Also

- [class var discretePositionCount: Int](gcdualsenseadaptivetrigger/discretepositioncount.md)
  The number of discrete control positions that the DualSense adaptive triggers support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdualsenseadaptivetrigger/armposition)*