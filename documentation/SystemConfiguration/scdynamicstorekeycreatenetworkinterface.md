# SCDynamicStoreKeyCreateNetworkInterface(_:_:)

**Framework**: System Configuration  
**Kind**: func

Creates a dynamic store key that can be used to access the network interface configuration information in the dynamic store.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCDynamicStoreKeyCreateNetworkInterface(_ allocator: CFAllocator?, _ domain: CFString) -> CFString
```

#### Return Value

A string containing the formatted key.

## Parameters

- `allocator`: The allocator that should be used to allocate memory for this key. This parameter may be   in which case the current default allocator is used. If this value is not a valid  , the behavior is undefined.
- `domain`: The desired domain, such as the requested configuration or the current state.

## See Also

- [func SCDynamicStoreKeyCreateNetworkGlobalEntity(CFAllocator?, CFString, CFString) -> CFString](scdynamicstorekeycreatenetworkglobalentity(_:_:_:).md)
  Creates a dynamic store key that can be used to access a specific global (as opposed to a per-service or per-interface) network configuration entity.
- [func SCDynamicStoreKeyCreateNetworkInterfaceEntity(CFAllocator?, CFString, CFString, CFString?) -> CFString](scdynamicstorekeycreatenetworkinterfaceentity(_:_:_:_:).md)
  Creates a dynamic store key that can be used to access the per-interface network configuration information in the dynamic store.
- [func SCDynamicStoreKeyCreateNetworkServiceEntity(CFAllocator?, CFString, CFString, CFString?) -> CFString](scdynamicstorekeycreatenetworkserviceentity(_:_:_:_:).md)
  Creates a dynamic store key that can be used to access the per-service network configuration information.
- [func SCDynamicStoreKeyCreateComputerName(CFAllocator?) -> CFString](scdynamicstorekeycreatecomputername(_:).md)
  Creates a key that can be used to receive notifications when the current computer name changes.
- [func SCDynamicStoreKeyCreateConsoleUser(CFAllocator?) -> CFString](scdynamicstorekeycreateconsoleuser(_:).md)
  Creates a key that can be used to receive notifications when the current console user changes.
- [func SCDynamicStoreKeyCreateHostNames(CFAllocator?) -> CFString](scdynamicstorekeycreatehostnames(_:).md)
  Creates a key that can be used to receive notifications when the `HostNames` entity changes.
- [func SCDynamicStoreKeyCreateLocation(CFAllocator?) -> CFString](scdynamicstorekeycreatelocation(_:).md)
  Creates a key that can be used to receive notifications when the location identifier changes.
- [func SCDynamicStoreKeyCreateProxies(CFAllocator?) -> CFString](scdynamicstorekeycreateproxies(_:).md)
  Creates a key that can be used to receive notifications when the current network proxy settings are changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorekeycreatenetworkinterface(_:_:))*