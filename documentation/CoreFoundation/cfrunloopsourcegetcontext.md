# CFRunLoopSourceGetContext(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the context information for a CFRunLoopSource object.

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
func CFRunLoopSourceGetContext(_ source: CFRunLoopSource!, _ context: UnsafeMutablePointer<CFRunLoopSourceContext>!)
```

#### Discussion

Run loop sources come in two versions with different-sized context structures. `context` must point to the correct version of the structure for `source`. Before calling this function, you need to initialize the `version` member of `context` with the version number (either 0 or 1) of `source`.

## Parameters

- `source`: The run loop source to examine.
- `context`: A pointer to the structure into which the context information for   is to be copied. The information being returned is the same information passed to   when creating  .

## See Also

- [func CFRunLoopSourceCreate(CFAllocator!, CFIndex, UnsafeMutablePointer<CFRunLoopSourceContext>!) -> CFRunLoopSource!](cfrunloopsourcecreate(_:_:_:).md)
  Creates a CFRunLoopSource object.
- [func CFRunLoopSourceGetOrder(CFRunLoopSource!) -> CFIndex](cfrunloopsourcegetorder(_:).md)
  Returns the ordering parameter for a CFRunLoopSource object.
- [func CFRunLoopSourceGetTypeID() -> CFTypeID](cfrunloopsourcegettypeid().md)
  Returns the type identifier of the CFRunLoopSource opaque type.
- [func CFRunLoopSourceInvalidate(CFRunLoopSource!)](cfrunloopsourceinvalidate(_:).md)
  Invalidates a CFRunLoopSource object, stopping it from ever firing again.
- [func CFRunLoopSourceIsValid(CFRunLoopSource!) -> Bool](cfrunloopsourceisvalid(_:).md)
  Returns a Boolean value that indicates whether a CFRunLoopSource object is valid and able to fire.
- [func CFRunLoopSourceSignal(CFRunLoopSource!)](cfrunloopsourcesignal(_:).md)
  Signals a CFRunLoopSource object, marking it as ready to fire.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcegetcontext(_:_:))*