# GLKVector4MakeWithArray(_:)

**Framework**: GLKit  
**Kind**: func

Returns a new four-component vector created from an array of components.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKVector4MakeWithArray(_ values: UnsafeMutablePointer<Float>!) -> GLKVector4
```

#### Return Value

The array

#### Discussion

An initialized vector.

## Parameters

- `values`: The array containing the component values.

## See Also

- [func GLKVector4Make(Float, Float, Float, Float) -> GLKVector4](glkvector4make(_:_:_:_:).md)
  Returns a new four-component vector created from individual component values.
- [func GLKVector4MakeWithVector3(GLKVector3, Float) -> GLKVector4](glkvector4makewithvector3(_:_:).md)
  Returns a new four-component vector created by combining a three-component vector with a scalar value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkvector4makewitharray(_:))*