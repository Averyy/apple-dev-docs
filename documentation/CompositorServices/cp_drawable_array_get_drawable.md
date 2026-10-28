# cp_drawable_array_get_drawable

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the drawable at the specified index in the array.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
cp_drawable_tcp_drawable_array_get_drawable(cp_drawable_array_t drawable_array, size_t index);
```

## Return Value

The drawable available for drawing at the specified index.

## Discussion

The [`cp_drawable_t`](./cp_drawable_t.md) type contains the textures and other information you need to set up your render descriptor in Metal.

## Parameters

- `drawable_array`: The drawable array for a frame.
- `index`: The index of the drawable you want. The index must be greater than or equal to `0` and less than the value that [`cp_drawable_array_get_count`](./cp_drawable_array_get_count.md) returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_drawable_array_get_drawable)*