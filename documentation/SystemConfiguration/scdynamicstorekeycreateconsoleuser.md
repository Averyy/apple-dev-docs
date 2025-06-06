# SCDynamicStoreKeyCreateConsoleUser(_:)

**Framework**: System Configuration  
**Kind**: func

Creates a key that can be used to receive notifications when the current console user changes.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCDynamicStoreKeyCreateConsoleUser(_ allocator: CFAllocator?) -> CFString
```

#### Return Value

A notification string for the current console user.

#### Discussion

Use this key with the [`SCDynamicStoreSetNotificationKeys(_:_:_:)`](scdynamicstoresetnotificationkeys(_:_:_:).md) function.

## Parameters

- `allocator`: The allocator that should be used to allocate memory for this key. This parameter may be   in which case the current default allocator is used. If this value is not a valid  , the behavior is undefined.

## See Also

- [func SCDynamicStoreKeyCreateNetworkGlobalEntity(CFAllocator?, CFString, CFString) -> CFString](scdynamicstorekeycreatenetworkglobalentity(_:_:_:).md)
  Creates a dynamic store key that can be used to access a specific global (as opposed to a per-service or per-interface) network configuration entity.
- [func SCDynamicStoreKeyCreateNetworkInterface(CFAllocator?, CFString) -> CFString](scdynamicstorekeycreatenetworkinterface(_:_:).md)
  Creates a dynamic store key that can be used to access the network interface configuration information in the dynamic store.
- [func SCDynamicStoreKeyCreateNetworkInterfaceEntity(CFAllocator?, CFString, CFString, CFString?) -> CFString](scdynamicstorekeycreatenetworkinterfaceentity(_:_:_:_:).md)
  Creates a dynamic store key that can be used to access the per-interface network configuration information in the dynamic store.
- [func SCDynamicStoreKeyCreateNetworkServiceEntity(CFAllocator?, CFString, CFString, CFString?) -> CFString](scdynamicstorekeycreatenetworkserviceentity(_:_:_:_:).md)
  Creates a dynamic store key that can be used to access the per-service network configuration information.
- [func SCDynamicStoreKeyCreateComputerName(CFAllocator?) -> CFString](scdynamicstorekeycreatecomputername(_:).md)
  Creates a key that can be used to receive notifications when the current computer name changes.
- [func SCDynamicStoreKeyCreateHostNames(CFAllocator?) -> CFString](scdynamicstorekeycreatehostnames(_:).md)
  Creates a key that can be used to receive notifications when the `HostNames` entity changes.
- [func SCDynamicStoreKeyCreateLocation(CFAllocator?) -> CFString](scdynamicstorekeycreatelocation(_:).md)
  Creates a key that can be used to receive notifications when the location identifier changes.
- [func SCDynamicStoreKeyCreateProxies(CFAllocator?) -> CFString](scdynamicstorekeycreateproxies(_:).md)
  Creates a key that can be used to receive notifications when the current network proxy settings are changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorekeycreateconsoleuser(_:))*