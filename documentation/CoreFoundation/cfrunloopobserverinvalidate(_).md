# CFRunLoopObserverInvalidate(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Invalidates a CFRunLoopObserver object, stopping it from ever firing again.

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
func CFRunLoopObserverInvalidate(_ observer: CFRunLoopObserver!)
```

```c
extern void CFRunLoopObserverInvalidate(CFRunLoopObserverRef observer);
```

#### Discussion

Once invalidated, `observer` will never fire and call its callback function again. This function automatically removes `observer` from all run loop modes in which it had been added. The memory is not deallocated unless the run loop held the only reference to `observer`.

## Parameters

- `observer`: The run loop observer to invalidate.

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
- [func CFRunLoopObserverGetContext(CFRunLoopObserver!, UnsafeMutablePointer<CFRunLoopObserverContext>!)](./cfrunloopobservergetcontext%28_,_%29.md)
  Returns the context information for a CFRunLoopObserver object.
- [func CFRunLoopObserverGetOrder(CFRunLoopObserver!) -> CFIndex](./cfrunloopobservergetorder%28_%29.md)
  Returns the ordering parameter for a CFRunLoopObserver object.
- [func CFRunLoopObserverGetTypeID() -> CFTypeID](./cfrunloopobservergettypeid%28%29.md)
  Returns the type identifier for the CFRunLoopObserver opaque type.
- [func CFRunLoopObserverIsValid(CFRunLoopObserver!) -> Bool](./cfrunloopobserverisvalid%28_%29.md)
  Returns a Boolean value that indicates whether a CFRunLoopObserver object is valid and able to fire.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopobserverinvalidate(_:))*