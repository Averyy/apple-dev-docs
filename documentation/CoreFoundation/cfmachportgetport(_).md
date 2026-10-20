# CFMachPortGetPort(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the native Mach port represented by a CFMachPort object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFMachPortGetPort(_ port: CFMachPort!) -> mach_port_t
```

```c
extern mach_port_t CFMachPortGetPort(CFMachPortRef port);
```

#### Return Value

The native Mach port represented by `port`.

## Parameters

- `port`: The CFMachPort object to examine.

## See Also

### Examining a CFMachPort Object
- [func CFMachPortGetContext(CFMachPort!, UnsafeMutablePointer<CFMachPortContext>!)](./cfmachportgetcontext%28_,_%29.md)
  Returns the context information for a CFMachPort object.
- [func CFMachPortGetInvalidationCallBack(CFMachPort!) -> CFMachPortInvalidationCallBack!](./cfmachportgetinvalidationcallback%28_%29.md)
  Returns the invalidation callback function for a CFMachPort object.
- [func CFMachPortIsValid(CFMachPort!) -> Bool](./cfmachportisvalid%28_%29.md)
  Returns a Boolean value that indicates whether a CFMachPort object is valid and able to receive messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmachportgetport(_:))*