# CFRunLoopRemoveSource(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Removes a CFRunLoopSource object from a run loop mode.

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
func CFRunLoopRemoveSource(_ rl: CFRunLoop!, _ source: CFRunLoopSource!, _ mode: CFRunLoopMode!)
```

#### Discussion

If `source` is a version 0 source, this function calls the `cancel` callback function specified in the context structure for `source`. See [`CFRunLoopSourceContext`](cfrunloopsourcecontext.md) and [`CFRunLoopSourceContext1`](cfrunloopsourcecontext1.md)for more details.

If `rl` does not contain `source` in `mode`, this function does nothing.

## Parameters

- `rl`: The run loop to modify.
- `source`: The run loop source to remove.
- `mode`: The run loop mode of   from which to remove  . Use the constant   to remove   from the set of objects monitored by all the common modes.

## See Also

- [func CFRunLoopAddSource(CFRunLoop!, CFRunLoopSource!, CFRunLoopMode!)](cfrunloopaddsource(_:_:_:).md)
  Adds a CFRunLoopSource object to a run loop mode.
- [func CFRunLoopContainsSource(CFRunLoop!, CFRunLoopSource!, CFRunLoopMode!) -> Bool](cfrunloopcontainssource(_:_:_:).md)
  Returns a Boolean value that indicates whether a run loop mode contains a particular CFRunLoopSource object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopremovesource(_:_:_:))*