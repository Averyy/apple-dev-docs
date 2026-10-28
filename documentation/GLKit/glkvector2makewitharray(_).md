# GLKVector2MakeWithArray(_:)

**Framework**: GLKit  
**Kind**: func  
**Role**: Function

Returns a new two-component vector created from an array of components.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func GLKVector2MakeWithArray(_ values: UnsafeMutablePointer<Float>!) -> GLKVector2
```

```c
static GLKVector2 GLKVector2MakeWithArray(float values[2]);
```

## Return Value

The array

## Discussion

An initialized vector.

## Parameters

- `values`: The array containing the component values.

## See Also

### Creating Vectors
- [func GLKVector2Make(Float, Float) -> GLKVector2](./glkvector2make%28_,_%29.md)
  Returns a new two-component vector created from individual component values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkvector2makewitharray(_:))*