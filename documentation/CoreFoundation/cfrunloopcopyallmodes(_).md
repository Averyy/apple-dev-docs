# CFRunLoopCopyAllModes(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns an array that contains all the defined modes for a CFRunLoop object.

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
func CFRunLoopCopyAllModes(_ rl: CFRunLoop!) -> CFArray!
```

#### Return Value

An array that contains all the run loop modes defined for `rl`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `rl`: The run loop to examine.

## See Also

- [func CFRunLoopAddCommonMode(CFRunLoop!, CFRunLoopMode!)](cfrunloopaddcommonmode(_:_:).md)
  Adds a mode to the set of run loop common modes.
- [func CFRunLoopCopyCurrentMode(CFRunLoop!) -> CFRunLoopMode!](cfrunloopcopycurrentmode(_:).md)
  Returns the name of the mode in which a given run loop is currently running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopcopyallmodes(_:))*