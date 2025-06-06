# ar_mesh_geometry_t

**Framework**: ARKit  
**Kind**: typealias

The shapes that make up a mesh anchor.

## Declaration

```swift
typedef NSObject<OS_ar_mesh_geometry> * ar_mesh_geometry_t;
```

## See Also

- [ar_geometry_primitive_type_t](ar_geometry_primitive_type_t.md)
  The kinds of geometry primitives that a geometry element can contain.
- [ar_geometry_element_get_buffer](ar_geometry_element_get_buffer.md)
  Gets a Metal buffer that contains index data that defines the geometry of an object.
- [ar_geometry_element_get_bytes_per_index](ar_geometry_element_get_bytes_per_index.md)
  Gets the number of bytes that represent an index value.
- [ar_geometry_element_get_count](ar_geometry_element_get_count.md)
  Gets the number of primitives in the Metal buffer for a geometry element.
- [ar_geometry_element_get_index_count_per_primitive](ar_geometry_element_get_index_count_per_primitive.md)
  Gets the number of indices for each primitive.
- [ar_geometry_element_get_primitive_type](ar_geometry_element_get_primitive_type.md)
  Gets the kind of primitive, lines or triangles, that a geometry element contains.
- [ar_geometry_source_get_buffer](ar_geometry_source_get_buffer.md)
  Gets a Metal buffer that contains per-vector data for a geometry source.
- [ar_geometry_source_get_components_per_vector](ar_geometry_source_get_components_per_vector.md)
  Gets the number of scalar components in each vector in a geometry source.
- [ar_geometry_source_get_count](ar_geometry_source_get_count.md)
  Gets the number of vectors in a geometry source.
- [ar_geometry_source_get_format](ar_geometry_source_get_format.md)
  Gets the vertex format for data in a geometry source’s buffer.
- [ar_geometry_source_get_offset](ar_geometry_source_get_offset.md)
  Gets the offset, in bytes, from the beginning of a geometry source’s buffer.
- [ar_geometry_source_get_stride](ar_geometry_source_get_stride.md)
  Gets the number of bytes between one vector and another in a geometry source’s buffer.
- [ar_geometry_primitive_type_line](ar_geometry_primitive_type_t/ar_geometry_primitive_type_line.md)
  Two vertices that connect to form a line.
- [ar_geometry_primitive_type_triangle](ar_geometry_primitive_type_t/ar_geometry_primitive_type_triangle.md)
  Three vertices that connect to form a triangle.
- [ar_geometry_element_t](ar_geometry_element_t.md)
  A container for vertex indices of lines or triangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_mesh_geometry_t)*