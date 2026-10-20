# CFMachPortInvalidate(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Invalidates a CFMachPort object, stopping it from receiving any more messages.

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
func CFMachPortInvalidate(_ port: CFMachPort!)
```

```c
extern void CFMachPortInvalidate(CFMachPortRef port);
```

#### Discussion

Invalidating a CFMachPort object prevents the port from ever receiving any more messages. The CFMachPort object is not deallocated, though. If the port has not already been invalidated, the port’s invalidation callback function is invoked, if one has been set with [`CFMachPortSetInvalidationCallBack(_:_:)`](./cfmachportsetinvalidationcallback%28_,_%29.md). The [`CFMachPortContext`](./cfmachportcontext.md)  `info` information for `port` is also released, if a release callback was specified in the port’s context structure. Finally, if a run loop source was created for `port`, the run loop source is invalidated, as well.

If the underlying Mach port is destroyed, the CFMachPort object is automatically invalidated.

## Parameters

- `port`: The CFMachPort object to invalidate.

## See Also

### Configuring a CFMachPort Object
- [func CFMachPortCreateRunLoopSource(CFAllocator!, CFMachPort!, CFIndex) -> CFRunLoopSource!](./cfmachportcreaterunloopsource%28_,_,_%29.md)
  Creates a CFRunLoopSource object for a CFMachPort object.
- [func CFMachPortSetInvalidationCallBack(CFMachPort!, CFMachPortInvalidationCallBack!)](./cfmachportsetinvalidationcallback%28_,_%29.md)
  Sets the callback function invoked when a CFMachPort object is invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmachportinvalidate(_:))*