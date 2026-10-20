# paths

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

An array containing the muted paths.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var paths: UnsafePointer<es_muted_path_t>!
```

```c
const es_muted_path_t * paths;
```

## See Also

### Accessing Muted Paths
- [struct es_muted_path_t](../es_muted_path_t.md)
  A structure that describes a path’s muted events.
- [var count: Int](./count.md)
  The number of elements in the paths array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_muted_paths_t/paths)*