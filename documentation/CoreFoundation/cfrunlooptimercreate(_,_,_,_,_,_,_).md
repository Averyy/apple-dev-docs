# CFRunLoopTimerCreate(_:_:_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a new CFRunLoopTimer object with a function callback.

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
func CFRunLoopTimerCreate(_ allocator: CFAllocator!, _ fireDate: CFAbsoluteTime, _ interval: CFTimeInterval, _ flags: CFOptionFlags, _ order: CFIndex, _ callout: CFRunLoopTimerCallBack!, _ context: UnsafeMutablePointer<CFRunLoopTimerContext>!) -> CFRunLoopTimer!
```

```c
extern CFRunLoopTimerRefCFRunLoopTimerCreate(CFAllocatorRef allocator, CFAbsoluteTime fireDate, CFTimeInterval interval, CFOptionFlags flags, CFIndex order, CFRunLoopTimerCallBack callout, CFRunLoopTimerContext *context);
```

## Return Value

The new CFRunLoopTimer object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

A timer needs to be added to a run loop mode before it will fire. To add the timer to a run loop, use [`CFRunLoopAddTimer(_:_:_:)`](./cfrunloopaddtimer%28_,_,_%29.md). A timer can be registered to only one run loop at a time, although it can be in multiple modes within that run loop.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass `NULL` or [`kCFAllocatorDefault`](./kcfallocatordefault.md) to use the current default allocator.
- `fireDate`: The time at which the timer should first fire. The fine precision (sub-millisecond at most) of the fire date may be adjusted slightly by the timer if there are implementation reasons to do so.
- `interval`: The firing interval of the timer. If `0` or negative, the timer fires once and then is automatically invalidated. The fine precision (sub-millisecond at most) of the interval may be adjusted slightly by the timer if implementation reasons to do so exist.
- `flags`: Currently ignored. Pass `0` for future compatibility.
- `order`: A priority index indicating the order in which run loop timers are processed. Run loop timers currently ignore this parameter. Pass `0`.
- `callout`: The callback function that is called when the timer fires.
- `context`: A structure holding contextual information for the run loop timer. The function copies the information out of the structure, so the memory pointed to by `context` does not need to persist beyond the function call. Can be `NULL` if the callback function does not need the context’s `info` pointer to keep track of state.

## See Also

### CFRunLoopTimer Miscellaneous Functions
- [func CFRunLoopTimerCreateWithHandler(CFAllocator!, CFAbsoluteTime, CFTimeInterval, CFOptionFlags, CFIndex, ((CFRunLoopTimer?) -> Void)!) -> CFRunLoopTimer!](./cfrunlooptimercreatewithhandler%28_,_,_,_,_,_%29.md)
  Creates a new CFRunLoopTimer object with a block-based handler.
- [func CFRunLoopTimerDoesRepeat(CFRunLoopTimer!) -> Bool](./cfrunlooptimerdoesrepeat%28_%29.md)
  Returns a Boolean value that indicates whether a CFRunLoopTimer object repeats.
- [func CFRunLoopTimerGetContext(CFRunLoopTimer!, UnsafeMutablePointer<CFRunLoopTimerContext>!)](./cfrunlooptimergetcontext%28_,_%29.md)
  Returns the context information for a CFRunLoopTimer object.
- [func CFRunLoopTimerGetInterval(CFRunLoopTimer!) -> CFTimeInterval](./cfrunlooptimergetinterval%28_%29.md)
  Returns the firing interval of a repeating CFRunLoopTimer object.
- [func CFRunLoopTimerGetNextFireDate(CFRunLoopTimer!) -> CFAbsoluteTime](./cfrunlooptimergetnextfiredate%28_%29.md)
  Returns the next firing time for a CFRunLoopTimer object.
- [func CFRunLoopTimerGetOrder(CFRunLoopTimer!) -> CFIndex](./cfrunlooptimergetorder%28_%29.md)
  Returns the ordering parameter for a CFRunLoopTimer object.
- [func CFRunLoopTimerGetTypeID() -> CFTypeID](./cfrunlooptimergettypeid%28%29.md)
  Returns the type identifier of the CFRunLoopTimer opaque type.
- [func CFRunLoopTimerInvalidate(CFRunLoopTimer!)](./cfrunlooptimerinvalidate%28_%29.md)
  Invalidates a CFRunLoopTimer object, stopping it from ever firing again.
- [func CFRunLoopTimerIsValid(CFRunLoopTimer!) -> Bool](./cfrunlooptimerisvalid%28_%29.md)
  Returns a Boolean value that indicates whether a CFRunLoopTimer object is valid and able to fire.
- [func CFRunLoopTimerSetNextFireDate(CFRunLoopTimer!, CFAbsoluteTime)](./cfrunlooptimersetnextfiredate%28_,_%29.md)
  Sets the next firing date for a CFRunLoopTimer object .


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunlooptimercreate(_:_:_:_:_:_:_:))*