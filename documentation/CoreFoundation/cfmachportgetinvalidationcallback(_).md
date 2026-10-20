# CFMachPortGetInvalidationCallBack(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the invalidation callback function for a CFMachPort object.

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
func CFMachPortGetInvalidationCallBack(_ port: CFMachPort!) -> CFMachPortInvalidationCallBack!
```

```c
extern CFMachPortInvalidationCallBackCFMachPortGetInvalidationCallBack(CFMachPortRef port);
```

#### Return Value

The callback function invoked when `port` is invalidated. `NULL` if no callback has been set with [`CFMachPortSetInvalidationCallBack(_:_:)`](./cfmachportsetinvalidationcallback%28_,_%29.md).

## Parameters

- `port`: The CFMachPort object to examine.

## See Also

### Examining a CFMachPort Object
- [func CFMachPortGetContext(CFMachPort!, UnsafeMutablePointer<CFMachPortContext>!)](./cfmachportgetcontext%28_,_%29.md)
  Returns the context information for a CFMachPort object.
- [func CFMachPortGetPort(CFMachPort!) -> mach_port_t](./cfmachportgetport%28_%29.md)
  Returns the native Mach port represented by a CFMachPort object.
- [func CFMachPortIsValid(CFMachPort!) -> Bool](./cfmachportisvalid%28_%29.md)
  Returns a Boolean value that indicates whether a CFMachPort object is valid and able to receive messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmachportgetinvalidationcallback(_:))*