# ar_geometry_element_is_equal_to_geometry_element

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Returns a bool value that indicates whether the two geometry elements are equal.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern bool ar_geometry_element_is_equal_to_geometry_element(ar_geometry_element_t geometry_element, ar_geometry_element_t other_geometry_element);
```

## Return Value

`YES` if the geometry elements are equal, otherwise `NO`.

## Parameters

- `geometry_element`: A geometry element to be compared.
- `other_geometry_element`: The other geometry element to be compared to.

## See Also

### Geometry functions
- [ar_geometry_source_is_equal_to_geometry_source](./ar_geometry_source_is_equal_to_geometry_source.md)
  Returns a bool value that indicates whether the two geometry sources are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_geometry_element_is_equal_to_geometry_element)*