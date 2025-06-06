# upstream

**Framework**: Combine  
**Kind**: property

The publisher from which this publisher receives elements.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
let upstream: Upstream
```

## See Also

- [let receiveSubscription: ((any Subscription) -> Bool)?](publishers/breakpoint/receivesubscription.md)
  A closure that executes when the publisher receives a subscription, and can raise a debugger signal by returning a true Boolean value.
- [let receiveOutput: ((Upstream.Output) -> Bool)?](publishers/breakpoint/receiveoutput.md)
  A closure that executes when the publisher receives output from the upstream publisher, and can raise a debugger signal by returning a true Boolean value.
- [let receiveCompletion: ((Subscribers.Completion<Publishers.Breakpoint<Upstream>.Failure>) -> Bool)?](publishers/breakpoint/receivecompletion.md)
  A closure that executes when the publisher receives completion, and can raise a debugger signal by returning a true Boolean value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/breakpoint/upstream)*