# CFRunLoopSourceGetOrder(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the ordering parameter for a CFRunLoopSource object.

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
func CFRunLoopSourceGetOrder(_ source: CFRunLoopSource!) -> CFIndex
```

```c
extern CFIndex CFRunLoopSourceGetOrder(CFRunLoopSourceRef source);
```

#### Return Value

The ordering parameter for `source`, which the run loop uses (for version 0 sources only) to determine the order in which sources are processed when multiple sources are firing.

## Parameters

- `source`: The run loop source to examine.

## See Also

### CFRunLoopSource Miscellaneous Functions
- [func CFRunLoopSourceCreate(CFAllocator!, CFIndex, UnsafeMutablePointer<CFRunLoopSourceContext>!) -> CFRunLoopSource!](./cfrunloopsourcecreate%28_,_,_%29.md)
  Creates a CFRunLoopSource object.
- [func CFRunLoopSourceGetContext(CFRunLoopSource!, UnsafeMutablePointer<CFRunLoopSourceContext>!)](./cfrunloopsourcegetcontext%28_,_%29.md)
  Returns the context information for a CFRunLoopSource object.
- [func CFRunLoopSourceGetTypeID() -> CFTypeID](./cfrunloopsourcegettypeid%28%29.md)
  Returns the type identifier of the CFRunLoopSource opaque type.
- [func CFRunLoopSourceInvalidate(CFRunLoopSource!)](./cfrunloopsourceinvalidate%28_%29.md)
  Invalidates a CFRunLoopSource object, stopping it from ever firing again.
- [func CFRunLoopSourceIsValid(CFRunLoopSource!) -> Bool](./cfrunloopsourceisvalid%28_%29.md)
  Returns a Boolean value that indicates whether a CFRunLoopSource object is valid and able to fire.
- [func CFRunLoopSourceSignal(CFRunLoopSource!)](./cfrunloopsourcesignal%28_%29.md)
  Signals a CFRunLoopSource object, marking it as ready to fire.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcegetorder(_:))*