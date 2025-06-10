# MPSGraphResizeNearestRoundingMode

**Framework**: Metal Performance Shaders Graph  
**Kind**: enum

The rounding mode to use when using nearest resize mode.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum MPSGraphResizeNearestRoundingMode
```

## Topics

### Enumeration Cases
- [MPSGraphResizeNearestRoundingMode.ceil](mpsgraphresizenearestroundingmode/ceil.md)
  Rounds values toward +inf.
- [MPSGraphResizeNearestRoundingMode.floor](mpsgraphresizenearestroundingmode/floor.md)
  Rounds values toward -inf.
- [MPSGraphResizeNearestRoundingMode.roundPreferCeil](mpsgraphresizenearestroundingmode/roundpreferceil.md)
  Rounds values to the nearest integer value, with 0.5f offset rounding toward +inf.
- [MPSGraphResizeNearestRoundingMode.roundPreferFloor](mpsgraphresizenearestroundingmode/roundpreferfloor.md)
  Rounds values to the nearest integer value, with 0.5f rounding toward -inf.
- [MPSGraphResizeNearestRoundingMode.roundToEven](mpsgraphresizenearestroundingmode/roundtoeven.md)
  Rounds values to the nearest integer value, with 0.5f rounding toward the closest even value.
- [MPSGraphResizeNearestRoundingMode.roundToOdd](mpsgraphresizenearestroundingmode/roundtoodd.md)
  Rounds values to the nearest integer value, with 0.5f rounding toward the closest odd value.
### Initializers
- [init?(rawValue: UInt)](mpsgraphresizenearestroundingmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphresizenearestroundingmode)*