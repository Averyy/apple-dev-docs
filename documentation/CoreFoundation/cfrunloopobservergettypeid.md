# CFRunLoopObserverGetTypeID()

**Framework**: Core Foundation  
**Kind**: func

Returns the type identifier for the CFRunLoopObserver opaque type.

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
func CFRunLoopObserverGetTypeID() -> CFTypeID
```

#### Return Value

The type identifier for the CFRunLoopObserver opaque type.

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
- [func CFRunLoopObserverInvalidate(CFRunLoopObserver!)](cfrunloopobserverinvalidate(_:).md)
  Invalidates a CFRunLoopObserver object, stopping it from ever firing again.
- [func CFRunLoopObserverIsValid(CFRunLoopObserver!) -> Bool](cfrunloopobserverisvalid(_:).md)
  Returns a Boolean value that indicates whether a CFRunLoopObserver object is valid and able to fire.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopobservergettypeid())*