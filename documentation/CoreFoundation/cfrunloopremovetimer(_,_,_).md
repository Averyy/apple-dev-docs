# CFRunLoopRemoveTimer(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Removes a CFRunLoopTimer object from a run loop mode.

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
func CFRunLoopRemoveTimer(_ rl: CFRunLoop!, _ timer: CFRunLoopTimer!, _ mode: CFRunLoopMode!)
```

```c
extern void CFRunLoopRemoveTimer(CFRunLoopRef rl, CFRunLoopTimerRef timer, CFRunLoopMode mode);
```

#### Discussion

If `rl` does not contain `timer` in `mode`, this function does nothing.

## Parameters

- `rl`: The run loop to modify.
- `timer`: The run loop timer to remove.
- `mode`: The run loop mode of `rl` from which to remove `timer`. Use the constant [`commonModes`](./cfrunloopmode/commonmodes.md) to remove `timer` from the set of objects monitored by all the common modes.

## See Also

### Managing Timers
- [func CFRunLoopAddTimer(CFRunLoop!, CFRunLoopTimer!, CFRunLoopMode!)](./cfrunloopaddtimer%28_,_,_%29.md)
  Adds a CFRunLoopTimer object to a run loop mode.
- [func CFRunLoopGetNextTimerFireDate(CFRunLoop!, CFRunLoopMode!) -> CFAbsoluteTime](./cfrunloopgetnexttimerfiredate%28_,_%29.md)
  Returns the time at which the next timer will fire.
- [func CFRunLoopContainsTimer(CFRunLoop!, CFRunLoopTimer!, CFRunLoopMode!) -> Bool](./cfrunloopcontainstimer%28_,_,_%29.md)
  Returns a Boolean value that indicates whether a run loop mode contains a particular CFRunLoopTimer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopremovetimer(_:_:_:))*