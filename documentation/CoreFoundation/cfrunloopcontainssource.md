# CFRunLoopContainsSource(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a Boolean value that indicates whether a run loop mode contains a particular CFRunLoopSource object.

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
func CFRunLoopContainsSource(_ rl: CFRunLoop!, _ source: CFRunLoopSource!, _ mode: CFRunLoopMode!) -> Bool
```

#### Return Value

`true` if `source` is in mode `mode` of the run loop `rl`, otherwise `false`.

#### Discussion

If `source` was added to [`commonModes`](cfrunloopmode/commonmodes.md), this function returns `true` if `mode` is either [`commonModes`](cfrunloopmode/commonmodes.md) or any of the modes that has been added to the set of common modes.

## Parameters

- `rl`: The run loop to examine.
- `source`: The run loop source for which to search.
- `mode`: The run loop mode of   in which to search. Use the constant   to search for   in the set of objects monitored by all the common modes.

## See Also

- [func CFRunLoopAddSource(CFRunLoop!, CFRunLoopSource!, CFRunLoopMode!)](cfrunloopaddsource(_:_:_:).md)
  Adds a CFRunLoopSource object to a run loop mode.
- [func CFRunLoopRemoveSource(CFRunLoop!, CFRunLoopSource!, CFRunLoopMode!)](cfrunloopremovesource(_:_:_:).md)
  Removes a CFRunLoopSource object from a run loop mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopcontainssource(_:_:_:))*