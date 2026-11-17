# ar_mesh_geometries_enumerator_t

**Framework**: ARKit  
**Kind**: typealias  
**Role**: Type Alias

Handler for enumerating a collection of mesh geometries.

**Availability**:
- visionOS 2.0+

## Declaration

```c
typedef _Bool (^)(NSObject<OS_ar_mesh_geometry> *) ar_mesh_geometries_enumerator_t;
```

## Return Value

`true` to continue enumerating, or `false` to stop enumerating.

## Parameters

- `mesh_geometry`: The mesh geometry.

## See Also

### Mesh geometry data types
- [ar_mesh_geometries_enumerator_function_t](./ar_mesh_geometries_enumerator_function_t.md)
  Function for enumerating a collection of mesh geometries.
- [ar_mesh_geometries_t](./ar_mesh_geometries_t.md)
  A collection of mesh geometries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_mesh_geometries_enumerator_t)*