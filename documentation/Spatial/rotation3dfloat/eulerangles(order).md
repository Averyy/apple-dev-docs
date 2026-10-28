# eulerAngles(order:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func eulerAngles(order: __SPEulerAngleOrder) -> EulerAnglesFloat
```

```c
static SPEulerAnglesFloat SPRotation3DFloatGetEulerAngles(SPRotation3DFloat rotation, SPEulerAngleOrder order);
```

## Return Value

A rotation structure.

## Discussion

Returns the Euler angles, in radians, from the specified rotation structure.

## Parameters

- `order`: The Euler angle ordering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3dfloat/eulerangles(order:))*