# GLKVector4Make(_:_:_:_:)

**Framework**: GLKit  
**Kind**: func

Returns a new four-component vector created from individual component values.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKVector4Make(_ x: Float, _ y: Float, _ z: Float, _ w: Float) -> GLKVector4
```

#### Return Value

An initialized vector.

## Parameters

- `x`: The first component.
- `y`: The second component.
- `z`: The third component.
- `w`: The fourth component.

## See Also

- [func GLKVector4MakeWithArray(UnsafeMutablePointer<Float>!) -> GLKVector4](glkvector4makewitharray(_:).md)
  Returns a new four-component vector created from an array of components.
- [func GLKVector4MakeWithVector3(GLKVector3, Float) -> GLKVector4](glkvector4makewithvector3(_:_:).md)
  Returns a new four-component vector created by combining a three-component vector with a scalar value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkvector4make(_:_:_:_:))*