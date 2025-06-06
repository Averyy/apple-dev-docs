# CFRunLoopSourceCreate(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a CFRunLoopSource object.

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
func CFRunLoopSourceCreate(_ allocator: CFAllocator!, _ order: CFIndex, _ context: UnsafeMutablePointer<CFRunLoopSourceContext>!) -> CFRunLoopSource!
```

#### Return Value

The new CFRunLoopSource object. You are responsible for releasing this object.

#### Discussion

The run loop source is not automatically added to a run loop. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `order`: A priority index indicating the order in which run loop sources are processed. When multiple run loop sources are firing in a single pass through the run loop, the sources are processed in increasing order of this parameter. If the run loop is set to process only one source per loop, only the highest priority source, the one with the lowest   value, is processed. This value is ignored for version 1 sources. Pass 0 unless there is a reason to do otherwise.
- `context`: A structure holding contextual information for the run loop source. The function copies the information out of the structure, so the memory pointed to by   does not need to persist beyond the function call.

## See Also

- [func CFRunLoopSourceGetContext(CFRunLoopSource!, UnsafeMutablePointer<CFRunLoopSourceContext>!)](cfrunloopsourcegetcontext(_:_:).md)
  Returns the context information for a CFRunLoopSource object.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecreate(_:_:_:))*