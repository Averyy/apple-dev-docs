# path_truncated

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether Endpoint Security truncated the path string.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var path_truncated: Bool
```

```c
bool path_truncated;
```

## Discussion

If Endpoint Security truncated the full file path when assigning the [`path`](./path.md) field, this value is `true`.

## See Also

### Inspecting File Properties
- [var path: es_string_token_t](./path.md)
  The file’s path.
- [var stat: stat](./stat.md)
  The file’s metadata, such as file size, user and group identifiers, and access and modification dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_file_t/path_truncated)*