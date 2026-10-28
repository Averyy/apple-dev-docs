# CFRunLoopContainsObserver(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether a run loop mode contains a particular CFRunLoopObserver object.

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
func CFRunLoopContainsObserver(_ rl: CFRunLoop!, _ observer: CFRunLoopObserver!, _ mode: CFRunLoopMode!) -> Bool
```

```c
extern Boolean CFRunLoopContainsObserver(CFRunLoopRef rl, CFRunLoopObserverRef observer, CFRunLoopMode mode);
```

## Return Value

`true` if `observer` is in mode `mode` of the run loop `rl`, otherwise `false`.

## Discussion

If `observer` was added to [`commonModes`](./cfrunloopmode/commonmodes.md), this function returns `true` if `mode` is either [`commonModes`](./cfrunloopmode/commonmodes.md) or any of the modes that has been added to the set of common modes.

## Parameters

- `rl`: The run loop to examine.
- `observer`: The run loop observer for which to search.
- `mode`: The run loop mode in which to search for `observer`. Use the constant [`commonModes`](./cfrunloopmode/commonmodes.md) to search for `observer` in the set of objects monitored by all the common modes.

## See Also

### Managing Observers
- [func CFRunLoopAddObserver(CFRunLoop!, CFRunLoopObserver!, CFRunLoopMode!)](./cfrunloopaddobserver%28_,_,_%29.md)
  Adds a CFRunLoopObserver object to a run loop mode.
- [func CFRunLoopRemoveObserver(CFRunLoop!, CFRunLoopObserver!, CFRunLoopMode!)](./cfrunloopremoveobserver%28_,_,_%29.md)
  Removes a CFRunLoopObserver object from a run loop mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopcontainsobserver(_:_:_:))*