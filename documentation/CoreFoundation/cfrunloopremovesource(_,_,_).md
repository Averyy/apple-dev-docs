# CFRunLoopRemoveSource(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Removes a CFRunLoopSource object from a run loop mode.

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
func CFRunLoopRemoveSource(_ rl: CFRunLoop!, _ source: CFRunLoopSource!, _ mode: CFRunLoopMode!)
```

```c
extern void CFRunLoopRemoveSource(CFRunLoopRef rl, CFRunLoopSourceRef source, CFRunLoopMode mode);
```

#### Discussion

If `source` is a version 0 source, this function calls the `cancel` callback function specified in the context structure for `source`. See [`CFRunLoopSourceContext`](./cfrunloopsourcecontext.md) and [`CFRunLoopSourceContext1`](./cfrunloopsourcecontext1.md)for more details.

If `rl` does not contain `source` in `mode`, this function does nothing.

## Parameters

- `rl`: The run loop to modify.
- `source`: The run loop source to remove.
- `mode`: The run loop mode of `rl` from which to remove `source`. Use the constant [`commonModes`](./cfrunloopmode/commonmodes.md) to remove `source` from the set of objects monitored by all the common modes.

## See Also

### Managing Sources
- [func CFRunLoopAddSource(CFRunLoop!, CFRunLoopSource!, CFRunLoopMode!)](./cfrunloopaddsource%28_,_,_%29.md)
  Adds a CFRunLoopSource object to a run loop mode.
- [func CFRunLoopContainsSource(CFRunLoop!, CFRunLoopSource!, CFRunLoopMode!) -> Bool](./cfrunloopcontainssource%28_,_,_%29.md)
  Returns a Boolean value that indicates whether a run loop mode contains a particular CFRunLoopSource object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopremovesource(_:_:_:))*