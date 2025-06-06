# CFRunLoopAddObserver(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Adds a CFRunLoopObserver object to a run loop mode.

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
func CFRunLoopAddObserver(_ rl: CFRunLoop!, _ observer: CFRunLoopObserver!, _ mode: CFRunLoopMode!)
```

#### Discussion

A run loop observer can be registered in only one run loop at a time, although it can be added to multiple run loop modes within that run loop.

If `rl` already contains `observer` in `mode`, this function does nothing.

## Parameters

- `rl`: The run loop to modify.
- `observer`: The run loop observer to add.
- `mode`: The run loop mode to which to add  . Use the constant   to add   to the set of objects monitored by all the common modes.

## See Also

- [func CFRunLoopContainsObserver(CFRunLoop!, CFRunLoopObserver!, CFRunLoopMode!) -> Bool](cfrunloopcontainsobserver(_:_:_:).md)
  Returns a Boolean value that indicates whether a run loop mode contains a particular CFRunLoopObserver object.
- [func CFRunLoopRemoveObserver(CFRunLoop!, CFRunLoopObserver!, CFRunLoopMode!)](cfrunloopremoveobserver(_:_:_:).md)
  Removes a CFRunLoopObserver object from a run loop mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopaddobserver(_:_:_:))*