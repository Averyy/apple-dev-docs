# CFRunLoopAddTimer(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Adds a CFRunLoopTimer object to a run loop mode.

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
func CFRunLoopAddTimer(_ rl: CFRunLoop!, _ timer: CFRunLoopTimer!, _ mode: CFRunLoopMode!)
```

```c
extern void CFRunLoopAddTimer(CFRunLoopRef rl, CFRunLoopTimerRef timer, CFRunLoopMode mode);
```

## Discussion

A run loop timer can be registered in only one run loop at a time, although it can be added to multiple run loop modes within that run loop.

If `rl` already contains `timer` in `mode`, this function does nothing.

## Parameters

- `rl`: The run loop to modify.
- `timer`: The run loop timer to add.
- `mode`: The run loop mode of `rl` to which to add `timer`. Use the constant [`commonModes`](./cfrunloopmode/commonmodes.md) to add `timer` to the set of objects monitored by all the common modes.

## See Also

### Managing Timers
- [func CFRunLoopGetNextTimerFireDate(CFRunLoop!, CFRunLoopMode!) -> CFAbsoluteTime](./cfrunloopgetnexttimerfiredate%28_,_%29.md)
  Returns the time at which the next timer will fire.
- [func CFRunLoopRemoveTimer(CFRunLoop!, CFRunLoopTimer!, CFRunLoopMode!)](./cfrunloopremovetimer%28_,_,_%29.md)
  Removes a CFRunLoopTimer object from a run loop mode.
- [func CFRunLoopContainsTimer(CFRunLoop!, CFRunLoopTimer!, CFRunLoopMode!) -> Bool](./cfrunloopcontainstimer%28_,_,_%29.md)
  Returns a Boolean value that indicates whether a run loop mode contains a particular CFRunLoopTimer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopaddtimer(_:_:_:))*