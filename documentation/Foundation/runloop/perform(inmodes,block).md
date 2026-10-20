# perform(inModes:block:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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
func perform(inModes modes: [RunLoop.Mode], block: @escaping @Sendable () -> Void)
```

```objc
- (void) performInModes:(NSArray<NSString *> *) modes block:(void (^)()) block;
```

## Parameters

- `modes`: An array of modes in which the run loop invokes the block.
- `block`: The block that the run loop invokes.

## See Also

### Scheduling and Canceling Tasks
- [func perform(() -> Void)](./perform%28_%29.md)
  Schedules a block that the run loop invokes.
- [func perform(Selector, target: Any, argument: Any?, order: Int, modes: [RunLoop.Mode])](./perform%28_,target,argument,order,modes%29.md)
  Schedules the sending of a message on the receiver.
- [func cancelPerform(Selector, target: Any, argument: Any?)](./cancelperform%28_,target,argument%29.md)
  Cancels the sending of a previously scheduled message.
- [func cancelPerformSelectors(withTarget: Any)](./cancelperformselectors%28withtarget%29.md)
  Cancels all outstanding ordered performs scheduled with a given target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/perform(inmodes:block:))*