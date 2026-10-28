# CFRunLoopGetNextTimerFireDate(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the time at which the next timer will fire.

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
func CFRunLoopGetNextTimerFireDate(_ rl: CFRunLoop!, _ mode: CFRunLoopMode!) -> CFAbsoluteTime
```

```c
extern CFAbsoluteTime CFRunLoopGetNextTimerFireDate(CFRunLoopRef rl, CFRunLoopMode mode);
```

## Return Value

The earliest firing time of the run loop timers registered in `mode` for the run loop `rl`.

## Parameters

- `rl`: The run loop to examine.
- `mode`: The run loop mode within `rl` to test.

## See Also

### Managing Timers
- [func CFRunLoopAddTimer(CFRunLoop!, CFRunLoopTimer!, CFRunLoopMode!)](./cfrunloopaddtimer%28_,_,_%29.md)
  Adds a CFRunLoopTimer object to a run loop mode.
- [func CFRunLoopRemoveTimer(CFRunLoop!, CFRunLoopTimer!, CFRunLoopMode!)](./cfrunloopremovetimer%28_,_,_%29.md)
  Removes a CFRunLoopTimer object from a run loop mode.
- [func CFRunLoopContainsTimer(CFRunLoop!, CFRunLoopTimer!, CFRunLoopMode!) -> Bool](./cfrunloopcontainstimer%28_,_,_%29.md)
  Returns a Boolean value that indicates whether a run loop mode contains a particular CFRunLoopTimer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopgetnexttimerfiredate(_:_:))*