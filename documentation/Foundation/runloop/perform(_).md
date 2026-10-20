# perform(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Schedules a block that the run loop invokes.

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
func perform(_ block: @escaping @Sendable () -> Void)
```

```objc
- (void) performBlock:(void (^)()) block;
```

## Parameters

- `block`: A block that the run loop invokes.

## See Also

### Scheduling and Canceling Tasks
- [func perform(inModes: [RunLoop.Mode], block: () -> Void)](./perform%28inmodes,block%29.md)
  Schedules a block that the run loop invokes when it’s running in any of the specified modes.
- [func perform(Selector, target: Any, argument: Any?, order: Int, modes: [RunLoop.Mode])](./perform%28_,target,argument,order,modes%29.md)
  Schedules the sending of a message on the receiver.
- [func cancelPerform(Selector, target: Any, argument: Any?)](./cancelperform%28_,target,argument%29.md)
  Cancels the sending of a previously scheduled message.
- [func cancelPerformSelectors(withTarget: Any)](./cancelperformselectors%28withtarget%29.md)
  Cancels all outstanding ordered performs scheduled with a given target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/perform(_:))*