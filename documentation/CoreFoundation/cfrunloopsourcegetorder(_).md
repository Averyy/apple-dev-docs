# CFRunLoopSourceGetOrder(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the ordering parameter for a CFRunLoopSource object.

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
func CFRunLoopSourceGetOrder(_ source: CFRunLoopSource!) -> CFIndex
```

#### Return Value

The ordering parameter for `source`, which the run loop uses (for version 0 sources only) to determine the order in which sources are processed when multiple sources are firing.

## Parameters

- `source`: The run loop source to examine.

## See Also

- [func CFRunLoopSourceCreate(CFAllocator!, CFIndex, UnsafeMutablePointer<CFRunLoopSourceContext>!) -> CFRunLoopSource!](cfrunloopsourcecreate(_:_:_:).md)
  Creates a CFRunLoopSource object.
- [func CFRunLoopSourceGetContext(CFRunLoopSource!, UnsafeMutablePointer<CFRunLoopSourceContext>!)](cfrunloopsourcegetcontext(_:_:).md)
  Returns the context information for a CFRunLoopSource object.
- [func CFRunLoopSourceGetTypeID() -> CFTypeID](cfrunloopsourcegettypeid().md)
  Returns the type identifier of the CFRunLoopSource opaque type.
- [func CFRunLoopSourceInvalidate(CFRunLoopSource!)](cfrunloopsourceinvalidate(_:).md)
  Invalidates a CFRunLoopSource object, stopping it from ever firing again.
- [func CFRunLoopSourceIsValid(CFRunLoopSource!) -> Bool](cfrunloopsourceisvalid(_:).md)
  Returns a Boolean value that indicates whether a CFRunLoopSource object is valid and able to fire.
- [func CFRunLoopSourceSignal(CFRunLoopSource!)](cfrunloopsourcesignal(_:).md)
  Signals a CFRunLoopSource object, marking it as ready to fire.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcegetorder(_:))*