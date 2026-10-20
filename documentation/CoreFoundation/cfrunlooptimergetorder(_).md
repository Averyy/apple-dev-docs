# CFRunLoopTimerGetOrder(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the ordering parameter for a CFRunLoopTimer object.

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
func CFRunLoopTimerGetOrder(_ timer: CFRunLoopTimer!) -> CFIndex
```

```c
extern CFIndex CFRunLoopTimerGetOrder(CFRunLoopTimerRef timer);
```

#### Return Value

The ordering parameter for `timer`.

#### Discussion

The ordering parameter is currently ignored by run loop timers.

## Parameters

- `timer`: The run loop timer to examine.

## See Also

### CFRunLoopTimer Miscellaneous Functions
- [func CFRunLoopTimerCreateWithHandler(CFAllocator!, CFAbsoluteTime, CFTimeInterval, CFOptionFlags, CFIndex, ((CFRunLoopTimer?) -> Void)!) -> CFRunLoopTimer!](./cfrunlooptimercreatewithhandler%28_,_,_,_,_,_%29.md)
  Creates a new CFRunLoopTimer object with a block-based handler.
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
- [func CFRunLoopTimerGetTypeID() -> CFTypeID](./cfrunlooptimergettypeid%28%29.md)
  Returns the type identifier of the CFRunLoopTimer opaque type.
- [func CFRunLoopTimerInvalidate(CFRunLoopTimer!)](./cfrunlooptimerinvalidate%28_%29.md)
  Invalidates a CFRunLoopTimer object, stopping it from ever firing again.
- [func CFRunLoopTimerIsValid(CFRunLoopTimer!) -> Bool](./cfrunlooptimerisvalid%28_%29.md)
  Returns a Boolean value that indicates whether a CFRunLoopTimer object is valid and able to fire.
- [func CFRunLoopTimerSetNextFireDate(CFRunLoopTimer!, CFAbsoluteTime)](./cfrunlooptimersetnextfiredate%28_,_%29.md)
  Sets the next firing date for a CFRunLoopTimer object .


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunlooptimergetorder(_:))*