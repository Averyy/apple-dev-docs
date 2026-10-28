# CFRunLoopSourceSignal(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Signals a CFRunLoopSource object, marking it as ready to fire.

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
func CFRunLoopSourceSignal(_ source: CFRunLoopSource!)
```

```c
extern void CFRunLoopSourceSignal(CFRunLoopSourceRef source);
```

## Discussion

This function has no effect on version 1 sources, which are automatically handled when Mach messages arrive for them. After signaling a version 0 source, you need to call [`CFRunLoopWakeUp(_:)`](./cfrunloopwakeup%28_%29.md) on one of the run loops in which the source is registered to get the source handled immediately.

## Parameters

- `source`: The run loop source to signal.

## See Also

### CFRunLoopSource Miscellaneous Functions
- [func CFRunLoopSourceCreate(CFAllocator!, CFIndex, UnsafeMutablePointer<CFRunLoopSourceContext>!) -> CFRunLoopSource!](./cfrunloopsourcecreate%28_,_,_%29.md)
  Creates a CFRunLoopSource object.
- [func CFRunLoopSourceGetContext(CFRunLoopSource!, UnsafeMutablePointer<CFRunLoopSourceContext>!)](./cfrunloopsourcegetcontext%28_,_%29.md)
  Returns the context information for a CFRunLoopSource object.
- [func CFRunLoopSourceGetOrder(CFRunLoopSource!) -> CFIndex](./cfrunloopsourcegetorder%28_%29.md)
  Returns the ordering parameter for a CFRunLoopSource object.
- [func CFRunLoopSourceGetTypeID() -> CFTypeID](./cfrunloopsourcegettypeid%28%29.md)
  Returns the type identifier of the CFRunLoopSource opaque type.
- [func CFRunLoopSourceInvalidate(CFRunLoopSource!)](./cfrunloopsourceinvalidate%28_%29.md)
  Invalidates a CFRunLoopSource object, stopping it from ever firing again.
- [func CFRunLoopSourceIsValid(CFRunLoopSource!) -> Bool](./cfrunloopsourceisvalid%28_%29.md)
  Returns a Boolean value that indicates whether a CFRunLoopSource object is valid and able to fire.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcesignal(_:))*