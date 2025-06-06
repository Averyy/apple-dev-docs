# CFRunLoopTimerInvalidate(_:)

**Framework**: Core Foundation  
**Kind**: func

Invalidates a CFRunLoopTimer object, stopping it from ever firing again.

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
func CFRunLoopTimerInvalidate(_ timer: CFRunLoopTimer!)
```

#### Discussion

Once invalidated, `timer` will never fire and call its callback function again. This function automatically removes `timer` from all run loop modes in which it had been added. The memory is not deallocated unless the run loop held the only reference to `timer`.

## Parameters

- `timer`: The run loop timer to invalidate.

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
- [func CFRunLoopTimerIsValid(CFRunLoopTimer!) -> Bool](cfrunlooptimerisvalid(_:).md)
  Returns a Boolean value that indicates whether a CFRunLoopTimer object is valid and able to fire.
- [func CFRunLoopTimerSetNextFireDate(CFRunLoopTimer!, CFAbsoluteTime)](cfrunlooptimersetnextfiredate(_:_:).md)
  Sets the next firing date for a CFRunLoopTimer object .


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunlooptimerinvalidate(_:))*