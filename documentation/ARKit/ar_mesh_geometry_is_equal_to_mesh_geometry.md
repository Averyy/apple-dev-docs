# ar_mesh_geometry_is_equal_to_mesh_geometry

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Returns a bool value that indicates whether the two mesh geometries are equal.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern bool ar_mesh_geometry_is_equal_to_mesh_geometry(ar_mesh_geometry_t mesh_geometry, ar_mesh_geometry_t other_mesh_geometry);
```

## Return Value

`YES` if the mesh geometries are equal, otherwise `NO`.

## Parameters

- `mesh_geometry`: A mesh geometry to be compared.
- `other_mesh_geometry`: The other mesh geometry to be compared to.

## See Also

### Mesh geometry functions
- [ar_mesh_geometries_enumerate_geometries](./ar_mesh_geometries_enumerate_geometries.md)
  Enumerate a collection of mesh geometries.
- [ar_mesh_geometries_enumerate_geometries_f](./ar_mesh_geometries_enumerate_geometries_f.md)
  Enumerates a collection of mesh geometries using a function.
- [ar_mesh_geometries_get_count](./ar_mesh_geometries_get_count.md)
  Get the count of mesh geometries in a collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_mesh_geometry_is_equal_to_mesh_geometry)*