# CFRunLoopObserverInvalidate(_:)

**Framework**: Core Foundation  
**Kind**: func

Invalidates a CFRunLoopObserver object, stopping it from ever firing again.

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
func CFRunLoopObserverInvalidate(_ observer: CFRunLoopObserver!)
```

#### Discussion

Once invalidated, `observer` will never fire and call its callback function again. This function automatically removes `observer` from all run loop modes in which it had been added. The memory is not deallocated unless the run loop held the only reference to `observer`.

## Parameters

- `observer`: The run loop observer to invalidate.

## See Also

- [func CFRunLoopObserverCreateWithHandler(CFAllocator!, CFOptionFlags, Bool, CFIndex, ((CFRunLoopObserver?, CFRunLoopActivity) -> Void)!) -> CFRunLoopObserver!](cfrunloopobservercreatewithhandler(_:_:_:_:_:).md)
  Creates a CFRunLoopObserver object with a block-based handler.
- [func CFRunLoopObserverCreate(CFAllocator!, CFOptionFlags, Bool, CFIndex, CFRunLoopObserverCallBack!, UnsafeMutablePointer<CFRunLoopObserverContext>!) -> CFRunLoopObserver!](cfrunloopobservercreate(_:_:_:_:_:_:).md)
  Creates a CFRunLoopObserver object with a function callback.
- [func CFRunLoopObserverDoesRepeat(CFRunLoopObserver!) -> Bool](cfrunloopobserverdoesrepeat(_:).md)
  Returns a Boolean value that indicates whether a CFRunLoopObserver repeats.
- [func CFRunLoopObserverGetActivities(CFRunLoopObserver!) -> CFOptionFlags](cfrunloopobservergetactivities(_:).md)
  Returns the run loop stages during which an observer runs.
- [func CFRunLoopObserverGetContext(CFRunLoopObserver!, UnsafeMutablePointer<CFRunLoopObserverContext>!)](cfrunloopobservergetcontext(_:_:).md)
  Returns the context information for a CFRunLoopObserver object.
- [func CFRunLoopObserverGetOrder(CFRunLoopObserver!) -> CFIndex](cfrunloopobservergetorder(_:).md)
  Returns the ordering parameter for a CFRunLoopObserver object.
- [func CFRunLoopObserverGetTypeID() -> CFTypeID](cfrunloopobservergettypeid().md)
  Returns the type identifier for the CFRunLoopObserver opaque type.
- [func CFRunLoopObserverIsValid(CFRunLoopObserver!) -> Bool](cfrunloopobserverisvalid(_:).md)
  Returns a Boolean value that indicates whether a CFRunLoopObserver object is valid and able to fire.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopobserverinvalidate(_:))*