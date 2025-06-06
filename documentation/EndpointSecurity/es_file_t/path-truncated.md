# path_truncated

**Framework**: Endpoint Security  
**Kind**: property

A Boolean value that indicates whether Endpoint Security truncated the path string.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var path_truncated: Bool
```

#### Discussion

If Endpoint Security truncated the full file path when assigning the [`path`](es_file_t/path.md) field, this value is `true`.

## See Also

- [var path: es_string_token_t](es_file_t/path.md)
  The file’s path.
- [var stat: stat](es_file_t/stat.md)
  The file’s metadata, such as file size, user and group identifiers, and access and modification dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_file_t/path_truncated)*