# CFMachPortGetContext(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the context information for a CFMachPort object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFMachPortGetContext(_ port: CFMachPort!, _ context: UnsafeMutablePointer<CFMachPortContext>!)
```

#### Discussion

The context version number for CFMachPort objects is currently `0`. Before calling this function, you need to initialize the `version` member of `context` to `0`.

## Parameters

- `port`: The CFMachPort object to examine.
- `context`: A pointer to the structure into which the context information for   is to be copied. The information being returned is usually the same information you passed to   or   when creating  . However, if   returned a cached CFMachPort object instead of creating a new object,   is filled with information from the original CFMachPort object instead of the information you passed to the function.

## See Also

- [func CFMachPortGetInvalidationCallBack(CFMachPort!) -> CFMachPortInvalidationCallBack!](cfmachportgetinvalidationcallback(_:).md)
  Returns the invalidation callback function for a CFMachPort object.
- [func CFMachPortGetPort(CFMachPort!) -> mach_port_t](cfmachportgetport(_:).md)
  Returns the native Mach port represented by a CFMachPort object.
- [func CFMachPortIsValid(CFMachPort!) -> Bool](cfmachportisvalid(_:).md)
  Returns a Boolean value that indicates whether a CFMachPort object is valid and able to receive messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmachportgetcontext(_:_:))*