# CFRunLoopTimerCreate(_:_:_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a new CFRunLoopTimer object with a function callback.

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
func CFRunLoopTimerCreate(_ allocator: CFAllocator!, _ fireDate: CFAbsoluteTime, _ interval: CFTimeInterval, _ flags: CFOptionFlags, _ order: CFIndex, _ callout: CFRunLoopTimerCallBack!, _ context: UnsafeMutablePointer<CFRunLoopTimerContext>!) -> CFRunLoopTimer!
```

#### Return Value

The new CFRunLoopTimer object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

A timer needs to be added to a run loop mode before it will fire. To add the timer to a run loop, use [`CFRunLoopAddTimer(_:_:_:)`](cfrunloopaddtimer(_:_:_:).md). A timer can be registered to only one run loop at a time, although it can be in multiple modes within that run loop.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or   to use the current default allocator.
- `fireDate`: The time at which the timer should first fire. The fine precision (sub-millisecond at most) of the fire date may be adjusted slightly by the timer if there are implementation reasons to do so.
- `interval`: The firing interval of the timer. If   or negative, the timer fires once and then is automatically invalidated. The fine precision (sub-millisecond at most) of the interval may be adjusted slightly by the timer if implementation reasons to do so exist.
- `flags`: Currently ignored. Pass   for future compatibility.
- `order`: A priority index indicating the order in which run loop timers are processed. Run loop timers currently ignore this parameter. Pass  .
- `callout`: The callback function that is called when the timer fires.
- `context`: A structure holding contextual information for the run loop timer. The function copies the information out of the structure, so the memory pointed to by   does not need to persist beyond the function call. Can be   if the callback function does not need the context’s   pointer to keep track of state.

## See Also

- [func CFRunLoopTimerCreateWithHandler(CFAllocator!, CFAbsoluteTime, CFTimeInterval, CFOptionFlags, CFIndex, ((CFRunLoopTimer?) -> Void)!) -> CFRunLoopTimer!](cfrunlooptimercreatewithhandler(_:_:_:_:_:_:).md)
  Creates a new CFRunLoopTimer object with a block-based handler.
- [func CFRunLoopTimerDoesRepeat(CFRunLoopTimer!) -> Bool](cfrunlooptimerdoesrepeat(_:).md)
  Returns a Boolean value that indicates whether a CFRunLoopTimer object repeats.
- [func CFRunLoopTimerGetContext(CFRunLoopTimer!, UnsafeMutablePointer<CFRunLoopTimerContext>!)](cfrunlooptimergetcontext(_:_:).md)
  Returns the context information for a CFRunLoopTimer object.
- [func CFRunLoopTimerGetInterval(CFRunLoopTimer!) -> CFTimeInterval](cfrunlooptimergetinterval(_:).md)
  Returns the firing interval of a repeating CFRunLoopTimer object.
- [func CFRunLoopTimerGetNextFireDate(CFRunLoopTimer!) -> CFAbsoluteTime](cfrunlooptimergetnextfiredate(_:).md)
  Returns the next firing time for a CFRunLoopTimer object.
- [func CFRunLoopTimerGetOrder(CFRunLoopTimer!) -> CFIndex](cfrunlooptimergetorder(_:).md)
  Returns the ordering parameter for a CFRunLoopTimer object.
- [func CFRunLoopTimerGetTypeID() -> CFTypeID](cfrunlooptimergettypeid().md)
  Returns the type identifier of the CFRunLoopTimer opaque type.
- [func CFRunLoopTimerInvalidate(CFRunLoopTimer!)](cfrunlooptimerinvalidate(_:).md)
  Invalidates a CFRunLoopTimer object, stopping it from ever firing again.
- [func CFRunLoopTimerIsValid(CFRunLoopTimer!) -> Bool](cfrunlooptimerisvalid(_:).md)
  Returns a Boolean value that indicates whether a CFRunLoopTimer object is valid and able to fire.
- [func CFRunLoopTimerSetNextFireDate(CFRunLoopTimer!, CFAbsoluteTime)](cfrunlooptimersetnextfiredate(_:_:).md)
  Sets the next firing date for a CFRunLoopTimer object .


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunlooptimercreate(_:_:_:_:_:_:_:))*