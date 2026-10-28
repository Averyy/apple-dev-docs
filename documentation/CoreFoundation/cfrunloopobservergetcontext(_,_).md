# CFRunLoopObserverGetContext(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the context information for a CFRunLoopObserver object.

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
func CFRunLoopObserverGetContext(_ observer: CFRunLoopObserver!, _ context: UnsafeMutablePointer<CFRunLoopObserverContext>!)
```

```c
extern void CFRunLoopObserverGetContext(CFRunLoopObserverRef observer, CFRunLoopObserverContext *context);
```

## Discussion

The context version number for run loop observers is currently `0`. Before calling this function, you need to initialize the `version` member of `context` to `0`.

## Parameters

- `observer`: The run loop observer to examine.
- `context`: Upon return, contains the context information for `observer`. This is the same information passed to [`CFRunLoopObserverCreate(_:_:_:_:_:_:)`](./cfrunloopobservercreate%28_,_,_,_,_,_%29.md) when creating `observer`.

## See Also

### CFRunLoopObserver Miscellaneous Functions
- [func CFRunLoopObserverCreateWithHandler(CFAllocator!, CFOptionFlags, Bool, CFIndex, ((CFRunLoopObserver?, CFRunLoopActivity) -> Void)!) -> CFRunLoopObserver!](./cfrunloopobservercreatewithhandler%28_,_,_,_,_%29.md)
  Creates a CFRunLoopObserver object with a block-based handler.
- [func CFRunLoopObserverCreate(CFAllocator!, CFOptionFlags, Bool, CFIndex, CFRunLoopObserverCallBack!, UnsafeMutablePointer<CFRunLoopObserverContext>!) -> CFRunLoopObserver!](./cfrunloopobservercreate%28_,_,_,_,_,_%29.md)
  Creates a CFRunLoopObserver object with a function callback.
- [func CFRunLoopObserverDoesRepeat(CFRunLoopObserver!) -> Bool](./cfrunloopobserverdoesrepeat%28_%29.md)
  Returns a Boolean value that indicates whether a CFRunLoopObserver repeats.
- [func CFRunLoopObserverGetActivities(CFRunLoopObserver!) -> CFOptionFlags](./cfrunloopobservergetactivities%28_%29.md)
  Returns the run loop stages during which an observer runs.
- [func CFRunLoopObserverGetOrder(CFRunLoopObserver!) -> CFIndex](./cfrunloopobservergetorder%28_%29.md)
  Returns the ordering parameter for a CFRunLoopObserver object.
- [func CFRunLoopObserverGetTypeID() -> CFTypeID](./cfrunloopobservergettypeid%28%29.md)
  Returns the type identifier for the CFRunLoopObserver opaque type.
- [func CFRunLoopObserverInvalidate(CFRunLoopObserver!)](./cfrunloopobserverinvalidate%28_%29.md)
  Invalidates a CFRunLoopObserver object, stopping it from ever firing again.
- [func CFRunLoopObserverIsValid(CFRunLoopObserver!) -> Bool](./cfrunloopobserverisvalid%28_%29.md)
  Returns a Boolean value that indicates whether a CFRunLoopObserver object is valid and able to fire.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopobservergetcontext(_:_:))*