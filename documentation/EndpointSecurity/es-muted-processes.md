# es_muted_processes(_:_:_:)

**Framework**: Endpoint Security  
**Kind**: func

Generates a list of muted processes.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func es_muted_processes(_ client: OpaquePointer, _ count: UnsafeMutablePointer<Int>, _ audit_tokens: UnsafeMutablePointer<UnsafeMutablePointer<audit_token_t>>?) -> es_return_t
```

#### Return Value

A value that indicates whether the request succeeded or failed with an error.

#### Discussion

The caller handles freeing the memory pointed to by `audit_token`.

## Parameters

- `client`: The client for which to generate a list of muted proceses.
- `count`: On return, the number of audit tokens generated.
- `audit_tokens`: On return, an array of audit tokens, each of which represents a muted process.

## See Also

- [func es_mute_path_literal(OpaquePointer, UnsafePointer<CChar>) -> es_return_t](es_mute_path_literal(_:_:).md)
  Suppresses events from executables matching a path literal.
- [func es_mute_path_prefix(OpaquePointer, UnsafePointer<CChar>) -> es_return_t](es_mute_path_prefix(_:_:).md)
  Suppresses events from executables matching a path prefix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_muted_processes(_:_:_:))*