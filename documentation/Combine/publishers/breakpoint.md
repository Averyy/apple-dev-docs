# Publishers.Breakpoint

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

A publisher that raises a debugger signal when a provided closure needs to stop the process in the debugger.

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
struct Breakpoint<Upstream> where Upstream : Publisher
```

#### Overview

When any of the provided closures returns `true`, this publisher raises the `SIGTRAP` signal to stop the process in the debugger. Otherwise, this publisher passes through values and completions as-is.

## Topics

### Creating a breakpoint publisher
- [init(upstream: Upstream, receiveSubscription: ((any Subscription) -> Bool)?, receiveOutput: ((Upstream.Output) -> Bool)?, receiveCompletion: ((Subscribers.Completion<Publishers.Breakpoint<Upstream>.Failure>) -> Bool)?)](./breakpoint/init%28upstream,receivesubscription,receiveoutput,receivecompletion%29.md)
  Creates a breakpoint publisher with the provided upstream publisher and breakpoint-raising closures.
### Declaring supporting types
- [Publishers.Breakpoint.Output](./breakpoint/output.md)
  The kind of values published by this publisher.
- [Publishers.Breakpoint.Failure](./breakpoint/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](./breakpoint/upstream.md)
  The publisher from which this publisher receives elements.
- [let receiveSubscription: ((any Subscription) -> Bool)?](./breakpoint/receivesubscription.md)
  A closure that executes when the publisher receives a subscription, and can raise a debugger signal by returning a true Boolean value.
- [let receiveOutput: ((Upstream.Output) -> Bool)?](./breakpoint/receiveoutput.md)
  A closure that executes when the publisher receives output from the upstream publisher, and can raise a debugger signal by returning a true Boolean value.
- [let receiveCompletion: ((Subscribers.Completion<Publishers.Breakpoint<Upstream>.Failure>) -> Bool)?](./breakpoint/receivecompletion.md)
  A closure that executes when the publisher receives completion, and can raise a debugger signal by returning a true Boolean value.

## Relationships

### Conforms To
- [Publisher](../publisher.md)

## See Also

### Debugging
- [Publishers.HandleEvents](./handleevents.md)
  A publisher that performs the specified closures when publisher events occur.
- [Publishers.Print](./print.md)
  A publisher that prints log messages for all publishing events, optionally prefixed with a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/breakpoint)*