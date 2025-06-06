# CFRunLoopAddSource(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Adds a CFRunLoopSource object to a run loop mode.

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
func CFRunLoopAddSource(_ rl: CFRunLoop!, _ source: CFRunLoopSource!, _ mode: CFRunLoopMode!)
```

#### Discussion

If `source` is a version 0 source, this function calls the `schedule` callback function specified in the context structure for `source`. See [`CFRunLoopSourceContext`](cfrunloopsourcecontext.md) for more details.

A run loop source can be registered in multiple run loops and run loop modes at the same time. When the source is signaled, whichever run loop that happens to detect the signal first will fire the source.

If `rl` already contains `source` in `mode`, this function does nothing.

## Parameters

- `rl`: The run loop to modify.
- `source`: The run loop source to add. The source is retained by the run loop.
- `mode`: The run loop mode to which to add  . Use the constant   to add   to the set of objects monitored by all the common modes.

## See Also

- [func CFRunLoopContainsSource(CFRunLoop!, CFRunLoopSource!, CFRunLoopMode!) -> Bool](cfrunloopcontainssource(_:_:_:).md)
  Returns a Boolean value that indicates whether a run loop mode contains a particular CFRunLoopSource object.
- [func CFRunLoopRemoveSource(CFRunLoop!, CFRunLoopSource!, CFRunLoopMode!)](cfrunloopremovesource(_:_:_:).md)
  Removes a CFRunLoopSource object from a run loop mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopaddsource(_:_:_:))*