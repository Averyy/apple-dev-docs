# SPAngleEqualToAngle

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether two angles are equal.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```c
static bool SPAngleEqualToAngle(SPAngle angle1, SPAngle angle2);
```

#### Return Value

A Boolean value that indicates whether two values are equal.

#### Discussion

Note that this function compares the raw value of each angle and doesn’t normalize the values. For example, 360° doesn’t equal 0°.

## Parameters

- `angle1`: The first angle value to compare.
- `angle2`: The second angle value to compare.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spangleequaltoangle)*