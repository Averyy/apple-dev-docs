# ar_mesh_geometries_enumerate_geometries

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Enumerate a collection of mesh geometries.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern void ar_mesh_geometries_enumerate_geometries(ar_mesh_geometries_t mesh_geometries, ar_mesh_geometries_enumerator_t mesh_geometries_enumerator);
```

## Parameters

- `mesh_geometries`: The collection of mesh geometries.
- `mesh_geometries_enumerator`: The enumerator handler.

## See Also

### Mesh geometry functions
- [ar_mesh_geometries_enumerate_geometries_f](./ar_mesh_geometries_enumerate_geometries_f.md)
  Enumerates a collection of mesh geometries using a function.
- [ar_mesh_geometries_get_count](./ar_mesh_geometries_get_count.md)
  Get the count of mesh geometries in a collection.
- [ar_mesh_geometry_is_equal_to_mesh_geometry](./ar_mesh_geometry_is_equal_to_mesh_geometry.md)
  Returns a bool value that indicates whether the two mesh geometries are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_mesh_geometries_enumerate_geometries)*