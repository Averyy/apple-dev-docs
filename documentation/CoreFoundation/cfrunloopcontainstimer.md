# CFRunLoopContainsTimer(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a Boolean value that indicates whether a run loop mode contains a particular CFRunLoopTimer object.

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
func CFRunLoopContainsTimer(_ rl: CFRunLoop!, _ timer: CFRunLoopTimer!, _ mode: CFRunLoopMode!) -> Bool
```

#### Return Value

`true` if `timer` is in mode `mode` of the run loop `rl`, `false` otherwise.

#### Discussion

If `timer` was added to [`commonModes`](cfrunloopmode/commonmodes.md), this function returns `true` if `mode` is either [`commonModes`](cfrunloopmode/commonmodes.md) or any of the modes that has been added to the set of common modes.

## Parameters

- `rl`: The run loop to examine.
- `timer`: The run loop timer for which to search.
- `mode`: The run loop mode of   in which to search for  . Use the constant   to search for   in the set of objects monitored by all the common modes.

## See Also

- [func CFRunLoopAddTimer(CFRunLoop!, CFRunLoopTimer!, CFRunLoopMode!)](cfrunloopaddtimer(_:_:_:).md)
  Adds a CFRunLoopTimer object to a run loop mode.
- [func CFRunLoopGetNextTimerFireDate(CFRunLoop!, CFRunLoopMode!) -> CFAbsoluteTime](cfrunloopgetnexttimerfiredate(_:_:).md)
  Returns the time at which the next timer will fire.
- [func CFRunLoopRemoveTimer(CFRunLoop!, CFRunLoopTimer!, CFRunLoopMode!)](cfrunloopremovetimer(_:_:_:).md)
  Removes a CFRunLoopTimer object from a run loop mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopcontainstimer(_:_:_:))*