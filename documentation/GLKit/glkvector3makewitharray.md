# GLKVector3MakeWithArray(_:)

**Framework**: GLKit  
**Kind**: func

Returns a new three-component vector created from an array of components.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKVector3MakeWithArray(_ values: UnsafeMutablePointer<Float>!) -> GLKVector3
```

#### Return Value

The array.

#### Discussion

An initialized vector.

## Parameters

- `values`: The array containing the component values.

## See Also

- [func GLKVector3Make(Float, Float, Float) -> GLKVector3](glkvector3make(_:_:_:).md)
  Returns a new three-component vector created from individual component values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkvector3makewitharray(_:))*