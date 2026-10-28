# CFRunLoopAddObserver(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Adds a CFRunLoopObserver object to a run loop mode.

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
func CFRunLoopAddObserver(_ rl: CFRunLoop!, _ observer: CFRunLoopObserver!, _ mode: CFRunLoopMode!)
```

```c
extern void CFRunLoopAddObserver(CFRunLoopRef rl, CFRunLoopObserverRef observer, CFRunLoopMode mode);
```

## Discussion

A run loop observer can be registered in only one run loop at a time, although it can be added to multiple run loop modes within that run loop.

If `rl` already contains `observer` in `mode`, this function does nothing.

## Parameters

- `rl`: The run loop to modify.
- `observer`: The run loop observer to add.
- `mode`: The run loop mode to which to add `observer`. Use the constant [`commonModes`](./cfrunloopmode/commonmodes.md) to add `observer` to the set of objects monitored by all the common modes.

## See Also

### Managing Observers
- [func CFRunLoopContainsObserver(CFRunLoop!, CFRunLoopObserver!, CFRunLoopMode!) -> Bool](./cfrunloopcontainsobserver%28_,_,_%29.md)
  Returns a Boolean value that indicates whether a run loop mode contains a particular CFRunLoopObserver object.
- [func CFRunLoopRemoveObserver(CFRunLoop!, CFRunLoopObserver!, CFRunLoopMode!)](./cfrunloopremoveobserver%28_,_,_%29.md)
  Removes a CFRunLoopObserver object from a run loop mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopaddobserver(_:_:_:))*