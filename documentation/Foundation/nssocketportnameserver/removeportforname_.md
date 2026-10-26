# removePortForName:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Unregisters the port for a given name on the local host.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Apple discourages the use of this symbol.

## Declaration

```objc
- (BOOL) removePortForName:(NSString *) name;
```

#### Return Value

[`true`](../../Swift/true.md) if successful, otherwise [`false`](../../Swift/false.md).

#### Discussion

If the operation is successful, the port can no longer be looked up using the name `portName`. Other applications that already have a reference to the port can continue to use it until it becomes invalid.

## Parameters

- `name`: The name of the port to unregister.

## See Also

### Registering and Removing Ports
- [- registerPort:name:](./registerport_name_.md)
  Registers a given port as a network service with the specified name in the local domain.
- [- registerPort:name:nameServerPortNumber:](./registerport_name_nameserverportnumber_.md)
  Registers a given port as a network service with the specified name in the local domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssocketportnameserver/removeportforname:)*