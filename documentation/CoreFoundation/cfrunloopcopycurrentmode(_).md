# CFRunLoopCopyCurrentMode(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the name of the mode in which a given run loop is currently running.

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
func CFRunLoopCopyCurrentMode(_ rl: CFRunLoop!) -> CFRunLoopMode!
```

```c
extern CFRunLoopModeCFRunLoopCopyCurrentMode(CFRunLoopRef rl);
```

## Return Value

The mode in which `rl` is currently running; `NULL` if `rl` is not running. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

When run on the current thread’s run loop, the returned value identifies the run loop mode that made the callout in which your code is currently executing.

## Parameters

- `rl`: The run loop to examine.

## See Also

### Managing Run Loop Modes
- [func CFRunLoopAddCommonMode(CFRunLoop!, CFRunLoopMode!)](./cfrunloopaddcommonmode%28_,_%29.md)
  Adds a mode to the set of run loop common modes.
- [func CFRunLoopCopyAllModes(CFRunLoop!) -> CFArray!](./cfrunloopcopyallmodes%28_%29.md)
  Returns an array that contains all the defined modes for a CFRunLoop object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopcopycurrentmode(_:))*