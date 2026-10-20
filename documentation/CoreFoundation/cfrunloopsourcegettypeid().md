# CFRunLoopSourceGetTypeID()

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the type identifier of the CFRunLoopSource opaque type.

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
func CFRunLoopSourceGetTypeID() -> CFTypeID
```

```c
extern CFTypeID CFRunLoopSourceGetTypeID();
```

#### Return Value

The type identifier for the CFRunLoopSource opaque type.

## See Also

### CFRunLoopSource Miscellaneous Functions
- [func CFRunLoopSourceCreate(CFAllocator!, CFIndex, UnsafeMutablePointer<CFRunLoopSourceContext>!) -> CFRunLoopSource!](./cfrunloopsourcecreate%28_,_,_%29.md)
  Creates a CFRunLoopSource object.
- [func CFRunLoopSourceGetContext(CFRunLoopSource!, UnsafeMutablePointer<CFRunLoopSourceContext>!)](./cfrunloopsourcegetcontext%28_,_%29.md)
  Returns the context information for a CFRunLoopSource object.
- [func CFRunLoopSourceGetOrder(CFRunLoopSource!) -> CFIndex](./cfrunloopsourcegetorder%28_%29.md)
  Returns the ordering parameter for a CFRunLoopSource object.
- [func CFRunLoopSourceInvalidate(CFRunLoopSource!)](./cfrunloopsourceinvalidate%28_%29.md)
  Invalidates a CFRunLoopSource object, stopping it from ever firing again.
- [func CFRunLoopSourceIsValid(CFRunLoopSource!) -> Bool](./cfrunloopsourceisvalid%28_%29.md)
  Returns a Boolean value that indicates whether a CFRunLoopSource object is valid and able to fire.
- [func CFRunLoopSourceSignal(CFRunLoopSource!)](./cfrunloopsourcesignal%28_%29.md)
  Signals a CFRunLoopSource object, marking it as ready to fire.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcegettypeid())*