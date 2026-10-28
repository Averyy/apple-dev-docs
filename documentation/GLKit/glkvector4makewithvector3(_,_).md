# GLKVector4MakeWithVector3(_:_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Returns a new four-component vector created by combining a three-component vector with a scalar value.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKVector4MakeWithVector3(_ vector: GLKVector3, _ w: Float) -> GLKVector4
```

```c
static GLKVector4 GLKVector4MakeWithVector3(GLKVector3 vector, float w);
```

## Return Value

A new vector.

## Parameters

- `vector`: A vector.
- `w`: The fourth component.

## See Also

### Creating Vectors
- [func GLKVector4Make(Float, Float, Float, Float) -> GLKVector4](./glkvector4make%28_,_,_,_%29.md)
  Returns a new four-component vector created from individual component values.
- [func GLKVector4MakeWithArray(UnsafeMutablePointer<Float>!) -> GLKVector4](./glkvector4makewitharray%28_%29.md)
  Returns a new four-component vector created from an array of components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkvector4makewithvector3(_:_:))*