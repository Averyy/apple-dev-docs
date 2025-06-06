# CFMachPortGetPort(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the native Mach port represented by a CFMachPort object.

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
func CFMachPortGetPort(_ port: CFMachPort!) -> mach_port_t
```

#### Return Value

The native Mach port represented by `port`.

## Parameters

- `port`: The CFMachPort object to examine.

## See Also

- [func CFMachPortGetContext(CFMachPort!, UnsafeMutablePointer<CFMachPortContext>!)](cfmachportgetcontext(_:_:).md)
  Returns the context information for a CFMachPort object.
- [func CFMachPortGetInvalidationCallBack(CFMachPort!) -> CFMachPortInvalidationCallBack!](cfmachportgetinvalidationcallback(_:).md)
  Returns the invalidation callback function for a CFMachPort object.
- [func CFMachPortIsValid(CFMachPort!) -> Bool](cfmachportisvalid(_:).md)
  Returns a Boolean value that indicates whether a CFMachPort object is valid and able to receive messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmachportgetport(_:))*