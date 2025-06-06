# nw_endpoint_t

**Framework**: Network  
**Kind**: typealias

A local or remote endpoint in a network connection.

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
typealias nw_endpoint_t = any OS_nw_endpoint
```

## Topics

### Endpoint Types
- [struct nw_endpoint_type_t](nw_endpoint_type_t.md)
  The type of a network endpoint, such as a host or a service.
- [func nw_endpoint_get_type(nw_endpoint_t) -> nw_endpoint_type_t](nw_endpoint_get_type(_:).md)
  Accesses the type of a endpoint.
### Host Endpoints
- [func nw_endpoint_create_host(UnsafePointer<CChar>, UnsafePointer<CChar>) -> nw_endpoint_t](nw_endpoint_create_host(_:_:).md)
  Creates a network endpoint with a hostname and port, where the hostname may be interpreted as an IP address.
- [func nw_endpoint_get_hostname(nw_endpoint_t) -> UnsafePointer<CChar>](nw_endpoint_get_hostname(_:).md)
  Accesses the hostname stored in an endpoint.
- [func nw_endpoint_get_port(nw_endpoint_t) -> UInt16](nw_endpoint_get_port(_:).md)
  Accesses the port stored in an endpoint, in host-byte order.
- [func nw_endpoint_copy_port_string(nw_endpoint_t) -> UnsafeMutablePointer<CChar>](nw_endpoint_copy_port_string(_:).md)
  Copies the port of an endpoint as a string.
### Address Endpoints
- [func nw_endpoint_create_address(UnsafePointer<sockaddr>) -> nw_endpoint_t](nw_endpoint_create_address(_:).md)
  Creates a network endpoint with an address structure.
- [func nw_endpoint_get_address(nw_endpoint_t) -> UnsafePointer<sockaddr>](nw_endpoint_get_address(_:).md)
  Accesses the address structure stored in an address endpoint.
- [func nw_endpoint_copy_address_string(nw_endpoint_t) -> UnsafeMutablePointer<CChar>](nw_endpoint_copy_address_string(_:).md)
  Copies the address of an endpoint as a string.
- [func nw_endpoint_copy_port_string(nw_endpoint_t) -> UnsafeMutablePointer<CChar>](nw_endpoint_copy_port_string(_:).md)
  Copies the port of an endpoint as a string.
### Bonjour Service Endpoints
- [func nw_endpoint_create_bonjour_service(UnsafePointer<CChar>, UnsafePointer<CChar>, UnsafePointer<CChar>) -> nw_endpoint_t](nw_endpoint_create_bonjour_service(_:_:_:).md)
  Creates a network endpoint with a Bonjour service name, type, and domain.
- [func nw_endpoint_get_bonjour_service_name(nw_endpoint_t) -> UnsafePointer<CChar>](nw_endpoint_get_bonjour_service_name(_:).md)
  Accesses the Bonjour service name stored in an endpoint.
- [func nw_endpoint_get_bonjour_service_type(nw_endpoint_t) -> UnsafePointer<CChar>](nw_endpoint_get_bonjour_service_type(_:).md)
  Accesses the Bonjour service type stored in an endpoint.
- [func nw_endpoint_get_bonjour_service_domain(nw_endpoint_t) -> UnsafePointer<CChar>](nw_endpoint_get_bonjour_service_domain(_:).md)
  Accesses the Bonjour service domain stored in an endpoint.
### URL Endpoints
- [func nw_endpoint_create_url(UnsafePointer<CChar>) -> nw_endpoint_t](nw_endpoint_create_url(_:).md)
  Creates a network endpoint with a URL string.
- [func nw_endpoint_get_url(nw_endpoint_t) -> UnsafePointer<CChar>](nw_endpoint_get_url(_:).md)
  Accesses the URL string stored in an endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_endpoint_t)*