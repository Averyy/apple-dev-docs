# CFRunLoopAddCommonMode(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Adds a mode to the set of run loop common modes.

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
func CFRunLoopAddCommonMode(_ rl: CFRunLoop!, _ mode: CFRunLoopMode!)
```

#### Discussion

Sources, timers, and observers get registered to one or more run loop modes and only run when the run loop is running in one of those modes. Common modes are a set of run loop modes for which you can define a set of sources, timers, and observers that are shared by these modes. Instead of registering a source, for example, to each specific run loop mode, you can register it once to the run loop’s common pseudo-mode and it will be automatically registered in each run loop mode in the common mode set. Likewise, when a mode is added to the set of common modes, any sources, timers, or observers already registered to the common pseudo-mode are added to the newly added common mode.

Once a mode is added to the set of common modes, it cannot be removed.

The Add, Contains, and Remove functions for sources, timers, and observers operate on a run loop’s set of common modes when you use the constant [`commonModes`](cfrunloopmode/commonmodes.md) for the run loop mode.

## Parameters

- `rl`: The run loop to modify. Each run loop has its own independent list of modes that are in the set of common modes.
- `mode`: The run loop mode to add to the set of common modes of  .

## See Also

- [func CFRunLoopCopyAllModes(CFRunLoop!) -> CFArray!](cfrunloopcopyallmodes(_:).md)
  Returns an array that contains all the defined modes for a CFRunLoop object.
- [func CFRunLoopCopyCurrentMode(CFRunLoop!) -> CFRunLoopMode!](cfrunloopcopycurrentmode(_:).md)
  Returns the name of the mode in which a given run loop is currently running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopaddcommonmode(_:_:))*