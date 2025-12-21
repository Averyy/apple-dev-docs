# run(mode:before:)

**Framework**: Foundation  
**Kind**: method

Runs the loop once, blocking for input in the specified mode until a given date.

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
func run(mode: RunLoop.Mode, before limitDate: Date) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the run loop ran and processed an input source or if the specified timeout value was reached; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false) if the run loop could not be started.

#### Discussion

If no input sources or timers are attached to the run loop, this method exits immediately and returns [`false`](https://developer.apple.com/documentation/Swift/false); otherwise, it returns after either the first input source is processed or `limitDate` is reached. Manually removing all known input sources and timers from the run loop does not guarantee that the run loop will exit immediately. macOS may install and remove additional input sources as needed to process requests targeted at the receiver’s thread. Those sources could therefore prevent the run loop from exiting.

> **Note**:  A timer is not considered an input source and may fire multiple times while waiting for this method to return

## Parameters

- `mode`: The mode in which to run. You may specify custom modes or use one of the modes listed in  .
- `limitDate`: The date until which to block.

## See Also

- [func run()](runloop/run.md)
  Puts the receiver into a permanent loop, during which time it processes data from all attached input sources.
- [func run(until: Date)](runloop/run(until:).md)
  Runs the loop until the specified date, during which time it processes data from all attached input sources.
- [func acceptInput(forMode: RunLoop.Mode, before: Date)](runloop/acceptinput(formode:before:).md)
  Runs the loop once or until the specified date, accepting input only for the specified mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/run(mode:before:))*