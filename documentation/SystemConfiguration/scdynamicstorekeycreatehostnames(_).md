# SCDynamicStoreKeyCreateHostNames(_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Creates a key that can be used to receive notifications when the `HostNames` entity changes.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SCDynamicStoreKeyCreateHostNames(_ allocator: CFAllocator?) -> CFString
```

```c
CFStringRefSCDynamicStoreKeyCreateHostNames(CFAllocatorRef allocator);
```

#### Return Value

A notification string for the `HostNames` entity.

#### Discussion

Use this key with the [`SCDynamicStoreSetNotificationKeys(_:_:_:)`](./scdynamicstoresetnotificationkeys%28_,_,_%29.md) function. Note that the `HostNames` entity includes the local host name.

## Parameters

- `allocator`: The allocator that should be used to allocate memory for this key. This parameter may be `NULL` in which case the current default allocator is used. If this value is not a valid [`CFAllocator`](../CoreFoundation/cfallocator.md), the behavior is undefined.

## See Also

### Group
- [func SCDynamicStoreKeyCreateNetworkGlobalEntity(CFAllocator?, CFString, CFString) -> CFString](./scdynamicstorekeycreatenetworkglobalentity%28_,_,_%29.md)
  Creates a dynamic store key that can be used to access a specific global (as opposed to a per-service or per-interface) network configuration entity.
- [func SCDynamicStoreKeyCreateNetworkInterface(CFAllocator?, CFString) -> CFString](./scdynamicstorekeycreatenetworkinterface%28_,_%29.md)
  Creates a dynamic store key that can be used to access the network interface configuration information in the dynamic store.
- [func SCDynamicStoreKeyCreateNetworkInterfaceEntity(CFAllocator?, CFString, CFString, CFString?) -> CFString](./scdynamicstorekeycreatenetworkinterfaceentity%28_,_,_,_%29.md)
  Creates a dynamic store key that can be used to access the per-interface network configuration information in the dynamic store.
- [func SCDynamicStoreKeyCreateNetworkServiceEntity(CFAllocator?, CFString, CFString, CFString?) -> CFString](./scdynamicstorekeycreatenetworkserviceentity%28_,_,_,_%29.md)
  Creates a dynamic store key that can be used to access the per-service network configuration information.
- [func SCDynamicStoreKeyCreateComputerName(CFAllocator?) -> CFString](./scdynamicstorekeycreatecomputername%28_%29.md)
  Creates a key that can be used to receive notifications when the current computer name changes.
- [func SCDynamicStoreKeyCreateConsoleUser(CFAllocator?) -> CFString](./scdynamicstorekeycreateconsoleuser%28_%29.md)
  Creates a key that can be used to receive notifications when the current console user changes.
- [func SCDynamicStoreKeyCreateLocation(CFAllocator?) -> CFString](./scdynamicstorekeycreatelocation%28_%29.md)
  Creates a key that can be used to receive notifications when the location identifier changes.
- [func SCDynamicStoreKeyCreateProxies(CFAllocator?) -> CFString](./scdynamicstorekeycreateproxies%28_%29.md)
  Creates a key that can be used to receive notifications when the current network proxy settings are changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorekeycreatehostnames(_:))*