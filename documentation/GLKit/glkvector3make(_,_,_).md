# GLKVector3Make(_:_:_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Returns a new three-component vector created from individual component values.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKVector3Make(_ x: Float, _ y: Float, _ z: Float) -> GLKVector3
```

```c
static GLKVector3 GLKVector3Make(float x, float y, float z);
```

#### Return Value

An initialized vector.

## Parameters

- `x`: The first component.
- `y`: The second component.
- `z`: The third component.

## See Also

### Creating Vectors
- [func GLKVector3MakeWithArray(UnsafeMutablePointer<Float>!) -> GLKVector3](./glkvector3makewitharray%28_%29.md)
  Returns a new three-component vector created from an array of components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkvector3make(_:_:_:))*