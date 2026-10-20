# nw_interface_t

**Framework**: Network  
**Kind**: typealias  
**Role**: Type Alias

An interface that a network connection uses to send and receive data.

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
typealias nw_interface_t = any OS_nw_interface
```

```c
typedef NSObject<OS_nw_interface> * nw_interface_t;
```

## Topics

### Network Interface Types
- [struct nw_interface_type_t](./nw_interface_type_t.md)
  Types of network interfaces, based on their link layer media types.
### Inspecting Interfaces
- [func nw_interface_get_type(nw_interface_t) -> nw_interface_type_t](./nw_interface_get_type%28_%29.md)
  Accesses the type of the interface, such as Wi-Fi or Loopback.
- [func nw_interface_get_name(nw_interface_t) -> UnsafePointer<CChar>](./nw_interface_get_name%28_%29.md)
  Accesses the name of the interface.
- [func nw_interface_get_index(nw_interface_t) -> UInt32](./nw_interface_get_index%28_%29.md)
  Accesses the system interface index associated with the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_interface_t)*