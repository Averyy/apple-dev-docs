# ar_mesh_geometries_enumerate_geometries_f

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Enumerates a collection of mesh geometries using a function.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern void ar_mesh_geometries_enumerate_geometries_f(ar_mesh_geometries_t mesh_geometries, void *context, ar_mesh_geometries_enumerator_function_t mesh_geometries_enumerator_function);
```

## Parameters

- `mesh_geometries`: The collection of mesh geometries.
- `context`: The application-defined context parameter to pass to the function.
- `mesh_geometries_enumerator_function`: The enumerator function.

## See Also

### Mesh geometry functions
- [ar_mesh_geometries_enumerate_geometries](./ar_mesh_geometries_enumerate_geometries.md)
  Enumerate a collection of mesh geometries.
- [ar_mesh_geometries_get_count](./ar_mesh_geometries_get_count.md)
  Get the count of mesh geometries in a collection.
- [ar_mesh_geometry_is_equal_to_mesh_geometry](./ar_mesh_geometry_is_equal_to_mesh_geometry.md)
  Returns a bool value that indicates whether the two mesh geometries are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_mesh_geometries_enumerate_geometries_f)*