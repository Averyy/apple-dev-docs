# ar_mesh_geometries_get_count

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Get the count of mesh geometries in a collection.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern size_t ar_mesh_geometries_get_count(ar_mesh_geometries_t mesh_geometries);
```

## Return Value

The number of mesh geometries in the collection.

## Parameters

- `mesh_geometries`: The collection of mesh geometries.

## See Also

### Mesh geometry functions
- [ar_mesh_geometries_enumerate_geometries](./ar_mesh_geometries_enumerate_geometries.md)
  Enumerate a collection of mesh geometries.
- [ar_mesh_geometries_enumerate_geometries_f](./ar_mesh_geometries_enumerate_geometries_f.md)
  Enumerates a collection of mesh geometries using a function.
- [ar_mesh_geometry_is_equal_to_mesh_geometry](./ar_mesh_geometry_is_equal_to_mesh_geometry.md)
  Returns a bool value that indicates whether the two mesh geometries are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_mesh_geometries_get_count)*