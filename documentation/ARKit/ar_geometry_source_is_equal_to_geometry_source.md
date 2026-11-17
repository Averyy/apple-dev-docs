# ar_geometry_source_is_equal_to_geometry_source

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Returns a bool value that indicates whether the two geometry sources are equal.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern bool ar_geometry_source_is_equal_to_geometry_source(ar_geometry_source_t geometry_source, ar_geometry_source_t other_geometry_source);
```

## Return Value

`YES` if the geometry sources are equal, otherwise `NO`.

## Parameters

- `geometry_source`: A geometry source to be compared.
- `other_geometry_source`: The other geometry source to be compared to.

## See Also

### Geometry functions
- [ar_geometry_element_is_equal_to_geometry_element](./ar_geometry_element_is_equal_to_geometry_element.md)
  Returns a bool value that indicates whether the two geometry elements are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_geometry_source_is_equal_to_geometry_source)*