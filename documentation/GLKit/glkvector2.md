# GLKVector2

**Framework**: GLKit  
**Kind**: typealias

A representation of a 2-component vector.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
typealias GLKVector2 = _GLKVector2
```

#### Overview

The `GLKVector2` type defines a 2-component floating-point vector as well as many mathematical operations commonly used to manipulate vectors. Graphics programming uses vectors extensively to represent positions, colors and other data structures.

The functions that manipulate `GLKVector2` structures treat the inputs as immutable, instead returning a new vector that represent the results of the operation.

##### Fields

| Name | Description |
| --- | --- |
| `x` | The first component in the vector. Typically used when the vector refers to a position. |
| `y` | The second component in the vector. Typically used when the vector refers to a position. |
| `s` | The first component in the vector. Typically used when the vector refers to texture coordinates. |
| `t` | The second component in the vector. Typically used when the vector refers to texture coordinates. |
| `v` | The elements of the vector expressed as an array. |


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkvector2)*