# perform(inModes:block:)

**Framework**: Foundation  
**Kind**: method

Schedules a block that the run loop invokes when it’s running in any of the specified modes.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func perform(inModes modes: [RunLoop.Mode], block: @escaping () -> Void)
```

## Parameters

- `modes`: An array of modes in which the run loop invokes the block.
- `block`: The block that the run loop invokes.

## See Also

- [func perform(() -> Void)](runloop/perform(_:).md)
  Schedules a block that the run loop invokes.
- [func perform(Selector, target: Any, argument: Any?, order: Int, modes: [RunLoop.Mode])](runloop/perform(_:target:argument:order:modes:).md)
  Schedules the sending of a message on the receiver.
- [func cancelPerform(Selector, target: Any, argument: Any?)](runloop/cancelperform(_:target:argument:).md)
  Cancels the sending of a previously scheduled message.
- [func cancelPerformSelectors(withTarget: Any)](runloop/cancelperformselectors(withtarget:).md)
  Cancels all outstanding ordered performs scheduled with a given target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/perform(inmodes:block:))*