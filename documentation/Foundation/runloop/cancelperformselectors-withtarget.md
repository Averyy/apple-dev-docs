# cancelPerformSelectors(withTarget:)

**Framework**: Foundation  
**Kind**: method

Cancels all outstanding ordered performs scheduled with a given target.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func cancelPerformSelectors(withTarget target: Any)
```

#### Discussion

This method cancels the previously scheduled messages associated with the target, ignoring the selector and argument of the scheduled operation. This is in contrast to [`cancelPerform(_:target:argument:)`](runloop/cancelperform(_:target:argument:).md), which requires you to match the selector and argument as well as the target. This method removes the perform requests for the object from all modes of the run loop.

## Parameters

- `target`: The previously-specified target.

## See Also

- [func perform(() -> Void)](runloop/perform(_:).md)
  Schedules a block that the run loop invokes.
- [func perform(inModes: [RunLoop.Mode], block: () -> Void)](runloop/perform(inmodes:block:).md)
  Schedules a block that the run loop invokes when it’s running in any of the specified modes.
- [func perform(Selector, target: Any, argument: Any?, order: Int, modes: [RunLoop.Mode])](runloop/perform(_:target:argument:order:modes:).md)
  Schedules the sending of a message on the receiver.
- [func cancelPerform(Selector, target: Any, argument: Any?)](runloop/cancelperform(_:target:argument:).md)
  Cancels the sending of a previously scheduled message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/cancelperformselectors(withtarget:))*