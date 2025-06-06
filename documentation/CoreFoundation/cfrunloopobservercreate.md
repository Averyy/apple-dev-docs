# CFRunLoopObserverCreate(_:_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a CFRunLoopObserver object with a function callback.

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
func CFRunLoopObserverCreate(_ allocator: CFAllocator!, _ activities: CFOptionFlags, _ repeats: Bool, _ order: CFIndex, _ callout: CFRunLoopObserverCallBack!, _ context: UnsafeMutablePointer<CFRunLoopObserverContext>!) -> CFRunLoopObserver!
```

#### Return Value

The new CFRunLoopObserver object. Ownership follows the Create Rule described in [`Ownership Policy`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148).

#### Discussion

The run loop observer is not automatically added to a run loop. To add the observer to a run loop, use [`CFRunLoopAddObserver(_:_:_:)`](cfrunloopaddobserver(_:_:_:).md). An observer can be registered to only one run loop, although it can be added to multiple run loop modes within that run loop.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or   to use the current default allocator.
- `activities`: Set of flags identifying the activity stages of the run loop during which the observer should be called. See  for the list of stages. To have the observer called at multiple stages in the run loop, combine the   values using the bitwise-OR operator.
- `repeats`: A flag identifying whether the observer should be called only once or every time through the run loop. If   is  , the observer is invalidated after it is called once, even if the observer was scheduled to be called at multiple stages within the run loop.
- `order`: A priority index indicating the order in which run loop observers are processed. When multiple run loop observers are scheduled in the same activity stage in a given run loop mode, the observers are processed in increasing order of this parameter. Pass 0 unless there is a reason to do otherwise.
- `callout`: The callback function invoked when the observer runs.
- `context`: A structure holding contextual information for the run loop observer. The function copies the information out of the structure, so the memory pointed to by   does not need to persist beyond the function call. Can be   if the observer does not need the context’s   pointer to keep track of state.

## See Also

- [func CFRunLoopObserverCreateWithHandler(CFAllocator!, CFOptionFlags, Bool, CFIndex, ((CFRunLoopObserver?, CFRunLoopActivity) -> Void)!) -> CFRunLoopObserver!](cfrunloopobservercreatewithhandler(_:_:_:_:_:).md)
  Creates a CFRunLoopObserver object with a block-based handler.
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
- [func CFRunLoopObserverInvalidate(CFRunLoopObserver!)](cfrunloopobserverinvalidate(_:).md)
  Invalidates a CFRunLoopObserver object, stopping it from ever firing again.
- [func CFRunLoopObserverIsValid(CFRunLoopObserver!) -> Bool](cfrunloopobserverisvalid(_:).md)
  Returns a Boolean value that indicates whether a CFRunLoopObserver object is valid and able to fire.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopobservercreate(_:_:_:_:_:_:))*