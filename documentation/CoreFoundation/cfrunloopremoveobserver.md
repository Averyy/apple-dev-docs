# CFRunLoopRemoveObserver(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Removes a CFRunLoopObserver object from a run loop mode.

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
func CFRunLoopRemoveObserver(_ rl: CFRunLoop!, _ observer: CFRunLoopObserver!, _ mode: CFRunLoopMode!)
```

#### Discussion

If `rl` does not contain `observer` in `mode`, this function does nothing.

## Parameters

- `rl`: The run loop to modify.
- `observer`: The run loop observer to remove.
- `mode`: The run loop mode of   from which to remove  . Use the constant   to remove   from the set of objects monitored by all the common modes.

## See Also

- [func CFRunLoopAddObserver(CFRunLoop!, CFRunLoopObserver!, CFRunLoopMode!)](cfrunloopaddobserver(_:_:_:).md)
  Adds a CFRunLoopObserver object to a run loop mode.
- [func CFRunLoopContainsObserver(CFRunLoop!, CFRunLoopObserver!, CFRunLoopMode!) -> Bool](cfrunloopcontainsobserver(_:_:_:).md)
  Returns a Boolean value that indicates whether a run loop mode contains a particular CFRunLoopObserver object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopremoveobserver(_:_:_:))*