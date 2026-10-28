# SCNMatrix4MakeRotation(_:_:_:_:)

**Framework**: SceneKit  
**Kind**: func  
**Role**: Function

Returns a matrix describing a rotation transformation.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
func SCNMatrix4MakeRotation(_ angle: Float, _ x: Float, _ y: Float, _ z: Float) -> SCNMatrix4
```

*macOS*

```swift
func SCNMatrix4MakeRotation(_ angle: CGFloat, _ x: CGFloat, _ y: CGFloat, _ z: CGFloat) -> SCNMatrix4
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```c
extern SCNMatrix4 SCNMatrix4MakeRotation(float angle, float x, float y, float z);
```

*macOS*

```c
extern SCNMatrix4 SCNMatrix4MakeRotation(CGFloat angle, CGFloat x, CGFloat y, CGFloat z);
```

## Return Value

A new rotation matrix.

## Parameters

- `angle`: The amount of rotation, in radians, measured counterclockwise around the rotation axis.
- `x`: The x-component of the rotation axis.
- `y`: The y-component of the rotation axis.
- `z`: The z-component of the rotation axis.

## See Also

### Creating Transform Matrices
- [func SCNMatrix4MakeTranslation(Float, Float, Float) -> SCNMatrix4](./scnmatrix4maketranslation%28_,_,_%29.md)
  Returns a matrix describing a translation transformation.
- [func SCNMatrix4MakeScale(Float, Float, Float) -> SCNMatrix4](./scnmatrix4makescale%28_,_,_%29.md)
  Returns a matrix describing a scale transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmatrix4makerotation(_:_:_:_:))*