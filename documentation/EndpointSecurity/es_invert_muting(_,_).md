# es_invert_muting(_:_:)

**Framework**: Endpoint Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 13.0+

## Declaration

```swift
func es_invert_muting(_ client: OpaquePointer, _ mute_type: es_mute_inversion_type_t) -> es_return_t
```

```c
extern es_return_t es_invert_muting(es_client_t *client, es_mute_inversion_type_t mute_type);
```

## See Also

### Functions
- [func es_muting_inverted(OpaquePointer, es_mute_inversion_type_t) -> es_mute_inverted_return_t](./es_muting_inverted%28_,_%29.md)
- [func es_unmute_all_target_paths(OpaquePointer) -> es_return_t](./es_unmute_all_target_paths%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_invert_muting(_:_:))*