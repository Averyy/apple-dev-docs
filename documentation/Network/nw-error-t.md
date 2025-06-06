# nw_error_t

**Framework**: Network  
**Kind**: typealias

The errors returned by the Network framework.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
typealias nw_error_t = any OS_nw_error
```

## Topics

### Inspecting Errors
- [func nw_error_get_error_domain(nw_error_t) -> nw_error_domain_t](nw_error_get_error_domain(_:).md)
  Accesses the domain of the network error.
- [struct nw_error_domain_t](nw_error_domain_t.md)
  The error domain for errors used by the Network framework.
- [func nw_error_get_error_code(nw_error_t) -> Int32](nw_error_get_error_code(_:).md)
  Accesses the specific code of the network error.
- [func nw_error_copy_cf_error(nw_error_t) -> Unmanaged<CFError>](nw_error_copy_cf_error(_:).md)
  Returns a copy of a network error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_error_t)*