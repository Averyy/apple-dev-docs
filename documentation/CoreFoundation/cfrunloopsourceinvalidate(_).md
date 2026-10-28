# CFRunLoopSourceInvalidate(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Invalidates a CFRunLoopSource object, stopping it from ever firing again.

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
func CFRunLoopSourceInvalidate(_ source: CFRunLoopSource!)
```

```c
extern void CFRunLoopSourceInvalidate(CFRunLoopSourceRef source);
```

## Discussion

Once invalidated, `source` will never fire and call its perform callback function again. This function automatically removes `source` from all the run loop modes in which it was registered. If `source` is a version 0 source, this function calls its `cancel` callback function as it is removed from each run loop mode. The memory for `source` is not deallocated unless the run loop held the only reference to `source`.

## Parameters

- `source`: The run loop source to invalidate.

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
- [func CFRunLoopSourceIsValid(CFRunLoopSource!) -> Bool](./cfrunloopsourceisvalid%28_%29.md)
  Returns a Boolean value that indicates whether a CFRunLoopSource object is valid and able to fire.
- [func CFRunLoopSourceSignal(CFRunLoopSource!)](./cfrunloopsourcesignal%28_%29.md)
  Signals a CFRunLoopSource object, marking it as ready to fire.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopsourceinvalidate(_:))*