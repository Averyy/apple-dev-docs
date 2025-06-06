# CFRunLoopTimerSetNextFireDate(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Sets the next firing date for a CFRunLoopTimer object .

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
func CFRunLoopTimerSetNextFireDate(_ timer: CFRunLoopTimer!, _ fireDate: CFAbsoluteTime)
```

#### Discussion

Resetting a timer’s next firing time is a relatively expensive operation and should not be done if it can be avoided; letting timers autorepeat is more efficient. In some cases, however, manually-adjusted, repeating timers are useful. For example, if you have an action that will be performed multiple times in the future, but at irregular time intervals, it would be very expensive to create, add to run loop modes, and then destroy a timer for each firing event. Instead, you can create a repeating timer with an initial firing time in the distant future (or the initial firing time) and a very large repeat interval—on the order of decades or more—and add it to all the necessary run loop modes. Then, when you know when the timer should fire next, you reset the firing time with [`CFRunLoopTimerSetNextFireDate(_:_:)`](cfrunlooptimersetnextfiredate(_:_:).md), perhaps from the timer’s own callback function. This technique effectively produces a reusable, asynchronous timer.

## Parameters

- `timer`: The run loop timer to modify.
- `fireDate`: The new firing time for  .

## See Also

- [func CFRunLoopTimerCreateWithHandler(CFAllocator!, CFAbsoluteTime, CFTimeInterval, CFOptionFlags, CFIndex, ((CFRunLoopTimer?) -> Void)!) -> CFRunLoopTimer!](cfrunlooptimercreatewithhandler(_:_:_:_:_:_:).md)
  Creates a new CFRunLoopTimer object with a block-based handler.
- [func CFRunLoopTimerCreate(CFAllocator!, CFAbsoluteTime, CFTimeInterval, CFOptionFlags, CFIndex, CFRunLoopTimerCallBack!, UnsafeMutablePointer<CFRunLoopTimerContext>!) -> CFRunLoopTimer!](cfrunlooptimercreate(_:_:_:_:_:_:_:).md)
  Creates a new CFRunLoopTimer object with a function callback.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunlooptimersetnextfiredate(_:_:))*