# CFRunLoopTimerCreateWithHandler(_:_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a new CFRunLoopTimer object with a block-based handler.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFRunLoopTimerCreateWithHandler(_ allocator: CFAllocator!, _ fireDate: CFAbsoluteTime, _ interval: CFTimeInterval, _ flags: CFOptionFlags, _ order: CFIndex, _ block: ((CFRunLoopTimer?) -> Void)!) -> CFRunLoopTimer!
```

```c
extern CFRunLoopTimerRefCFRunLoopTimerCreateWithHandler(CFAllocatorRef allocator, CFAbsoluteTime fireDate, CFTimeInterval interval, CFOptionFlags flags, CFIndex order, void (^block)(CFRunLoopTimerRef timer));
```

## Return Value

The new CFRunLoopTimer object. Ownership follows the Create Rule described in [Ownership Policy](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148).

## Discussion

A timer needs to be added to a run loop mode before it will fire. To add the timer to a run loop, use [`CFRunLoopAddTimer(_:_:_:)`](./cfrunloopaddtimer%28_,_,_%29.md). A timer can be registered to only one run loop at a time, although it can be in multiple modes within that run loop.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass `NULL` or [`kCFAllocatorDefault`](./kcfallocatordefault.md) to use the current default allocator.
- `fireDate`: The time at which the timer should first fire. The fine precision (sub-millisecond at most) of the fire date may be adjusted slightly by the timer if there are implementation reasons to do so.
- `interval`: The firing interval of the timer. If `0` or negative, the timer fires once and then is automatically invalidated. The fine precision (sub-millisecond at most) of the interval may be adjusted slightly by the timer if implementation reasons to do so exist.
- `flags`: Currently ignored. Pass `0` for future compatibility.
- `order`: A priority index indicating the order in which run loop timers are processed. Run loop timers currently ignore this parameter. Pass `0`.
- `block`: The block invoked when the timer fires. The block takes one argument:

  - **`timer`**: The run loop timer that is firing.

## See Also

### CFRunLoopTimer Miscellaneous Functions
- [func CFRunLoopTimerCreate(CFAllocator!, CFAbsoluteTime, CFTimeInterval, CFOptionFlags, CFIndex, CFRunLoopTimerCallBack!, UnsafeMutablePointer<CFRunLoopTimerContext>!) -> CFRunLoopTimer!](./cfrunlooptimercreate%28_,_,_,_,_,_,_%29.md)
  Creates a new CFRunLoopTimer object with a function callback.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunlooptimercreatewithhandler(_:_:_:_:_:_:))*