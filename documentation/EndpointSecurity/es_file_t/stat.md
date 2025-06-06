# stat

**Framework**: Endpoint Security  
**Kind**: property

The file’s metadata, such as file size, user and group identifiers, and access and modification dates.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var stat: stat
```

#### Discussion

The returned structure’s information is equivalent to that returned by the `stat(2)` system call.

## See Also

- [var path: es_string_token_t](es_file_t/path.md)
  The file’s path.
- [var path_truncated: Bool](es_file_t/path_truncated.md)
  A Boolean value that indicates whether Endpoint Security truncated the path string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_file_t/stat)*