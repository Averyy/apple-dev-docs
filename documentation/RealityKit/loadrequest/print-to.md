# print(_:to:)

**Framework**: RealityKit  
**Kind**: method

Prints log messages for all publishing events.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
func print(_ prefix: String = "", to stream: (any TextOutputStream)? = nil) -> Publishers.Print<Self>
```

#### Return Value

A publisher that prints log messages for all publishing events.

#### Discussion

Use `Publisher/print(_:to:)` to log messages the console.

In the example below, log messages are printed on the console:

```None
let integers = (1...2)
cancellable = integers.publisher
   .print("Logged a message", to: nil)
   .sink { _ in }

// Prints:
//  Logged a message: receive subscription: (1..<2)
//  Logged a message: request unlimited
//  Logged a message: receive value: (1)
//  Logged a message: receive finished
```

## Parameters

- `prefix`: A string —- which defaults to empty -— with which to prefix all log messages.
- `stream`: A stream for text output that receives messages, and which directs output to the console by default.  A custom stream can be used to log messages to other destinations.

## See Also

- [func breakpoint(receiveSubscription: ((any Subscription) -> Bool)?, receiveOutput: ((Self.Output) -> Bool)?, receiveCompletion: ((Subscribers.Completion<Self.Failure>) -> Bool)?) -> Publishers.Breakpoint<Self>](loadrequest/breakpoint(receivesubscription:receiveoutput:receivecompletion:).md)
  Raises a debugger signal when a provided closure needs to stop the process in the debugger.
- [func breakpointOnError() -> Publishers.Breakpoint<Self>](loadrequest/breakpointonerror.md)
  Raises a debugger signal upon receiving a failure.
- [func handleEvents(receiveSubscription: ((any Subscription) -> Void)?, receiveOutput: ((Self.Output) -> Void)?, receiveCompletion: ((Subscribers.Completion<Self.Failure>) -> Void)?, receiveCancel: (() -> Void)?, receiveRequest: ((Subscribers.Demand) -> Void)?) -> Publishers.HandleEvents<Self>](loadrequest/handleevents(receivesubscription:receiveoutput:receivecompletion:receivecancel:receiverequest:).md)
  Performs the specified closures when publisher events occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/loadrequest/print(_:to:))*