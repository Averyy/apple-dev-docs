# nw_framer_copy_local_endpoint(_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Accesses the local endpoint of the connection in which your protocol is running.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func nw_framer_copy_local_endpoint(_ framer: nw_framer_t) -> nw_endpoint_t
```

```c
nw_endpoint_tnw_framer_copy_local_endpoint(nw_framer_t framer);
```

## See Also

### Inspecting Instance Properties
- [func nw_framer_copy_remote_endpoint(nw_framer_t) -> nw_endpoint_t](./nw_framer_copy_remote_endpoint%28_%29.md)
  Accesses the remote endpoint of the connection in which your protocol is running.
- [func nw_framer_copy_parameters(nw_framer_t) -> nw_parameters_t](./nw_framer_copy_parameters%28_%29.md)
  Accesses the parameters of the connection in which your protocol is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_framer_copy_local_endpoint(_:))*