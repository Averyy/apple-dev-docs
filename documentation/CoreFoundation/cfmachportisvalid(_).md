# CFMachPortIsValid(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether a CFMachPort object is valid and able to receive messages.

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
func CFMachPortIsValid(_ port: CFMachPort!) -> Bool
```

```c
extern Boolean CFMachPortIsValid(CFMachPortRef port);
```

#### Return Value

`true` if `port` can be used for communication, otherwise `false`.

## Parameters

- `port`: The CFMachPort object to examine.

## See Also

### Examining a CFMachPort Object
- [func CFMachPortGetContext(CFMachPort!, UnsafeMutablePointer<CFMachPortContext>!)](./cfmachportgetcontext%28_,_%29.md)
  Returns the context information for a CFMachPort object.
- [func CFMachPortGetInvalidationCallBack(CFMachPort!) -> CFMachPortInvalidationCallBack!](./cfmachportgetinvalidationcallback%28_%29.md)
  Returns the invalidation callback function for a CFMachPort object.
- [func CFMachPortGetPort(CFMachPort!) -> mach_port_t](./cfmachportgetport%28_%29.md)
  Returns the native Mach port represented by a CFMachPort object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmachportisvalid(_:))*