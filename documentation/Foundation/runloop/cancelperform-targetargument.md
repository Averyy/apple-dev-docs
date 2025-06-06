# cancelPerform(_:target:argument:)

**Framework**: Foundation  
**Kind**: method

Cancels the sending of a previously scheduled message.

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
func cancelPerform(_ aSelector: Selector, target: Any, argument arg: Any?)
```

#### Discussion

You can use this method to cancel a message previously scheduled using the [`perform(_:target:argument:order:modes:)`](runloop/perform(_:target:argument:order:modes:).md) method. The parameters identify the message you want to cancel and must match those originally specified when the selector was scheduled. This method removes the perform request from all modes of the run loop.

## Parameters

- `aSelector`: The previously-specified selector.
- `target`: The previously-specified target.
- `arg`: The previously-specified argument.

## See Also

- [func perform(() -> Void)](runloop/perform(_:).md)
  Schedules a block that the run loop invokes.
- [func perform(inModes: [RunLoop.Mode], block: () -> Void)](runloop/perform(inmodes:block:).md)
  Schedules a block that the run loop invokes when it’s running in any of the specified modes.
- [func perform(Selector, target: Any, argument: Any?, order: Int, modes: [RunLoop.Mode])](runloop/perform(_:target:argument:order:modes:).md)
  Schedules the sending of a message on the receiver.
- [func cancelPerformSelectors(withTarget: Any)](runloop/cancelperformselectors(withtarget:).md)
  Cancels all outstanding ordered performs scheduled with a given target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/cancelperform(_:target:argument:))*