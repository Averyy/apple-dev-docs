# CFRunLoopSourceIsValid(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether a CFRunLoopSource object is valid and able to fire.

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
func CFRunLoopSourceIsValid(_ source: CFRunLoopSource!) -> Bool
```

```c
extern Boolean CFRunLoopSourceIsValid(CFRunLoopSourceRef source);
```

#### Return Value

`true` if `source` is valid, otherwise `false`.

## Parameters

- `source`: The run loop source to examine.

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
- [func CFRunLoopSourceSignal(CFRunLoopSource!)](./cfrunloopsourcesignal%28_%29.md)
  Signals a CFRunLoopSource object, marking it as ready to fire.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopsourceisvalid(_:))*