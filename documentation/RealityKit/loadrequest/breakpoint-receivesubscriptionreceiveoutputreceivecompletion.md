# breakpoint(receiveSubscription:receiveOutput:receiveCompletion:)

**Framework**: RealityKit  
**Kind**: method

Raises a debugger signal when a provided closure needs to stop the process in the debugger.

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
func breakpoint(receiveSubscription: ((any Subscription) -> Bool)? = nil, receiveOutput: ((Self.Output) -> Bool)? = nil, receiveCompletion: ((Subscribers.Completion<Self.Failure>) -> Bool)? = nil) -> Publishers.Breakpoint<Self>
```

#### Return Value

A publisher that raises a debugger signal when one of the provided closures returns `true`.

#### Discussion

Use `Publisher/breakpoint(receiveSubscription:receiveOutput:receiveCompletion:)` to examine one or more stages of the subscribe/publish/completion process and stop in the debugger, based on conditions you specify. When any of the provided closures returns `true`, this operator raises the `SIGTRAP` signal to stop the process in the debugger. Otherwise, this publisher passes through values and completions as-is.

In the example below, a `PassthroughSubject` publishes strings to a breakpoint republisher. When the breakpoint receives the string “`DEBUGGER`”, it returns `true`, which stops the app in the debugger.

```None
let publisher = PassthroughSubject<String?, Never>()
cancellable = publisher
    .breakpoint(
        receiveOutput: { value in return value == "DEBUGGER" }
    )
    .sink { print("\(String(describing: $0))" , terminator: " ") }

publisher.send("DEBUGGER")

// Prints: "error: Execution was interrupted, reason: signal SIGTRAP."
// Depending on your specific environment, the console messages may
// also include stack trace information, which is not shown here.
```

## Parameters

- `receiveSubscription`: A closure that executes when the publisher receives a subscription. Return   from this closure to raise  , or false to continue.
- `receiveOutput`: A closure that executes when the publisher receives a value. Return   from this closure to raise  , or false to continue.
- `receiveCompletion`: A closure that executes when the publisher receives a completion. Return   from this closure to raise  , or false to continue.

## See Also

- [func breakpointOnError() -> Publishers.Breakpoint<Self>](loadrequest/breakpointonerror.md)
  Raises a debugger signal upon receiving a failure.
- [func handleEvents(receiveSubscription: ((any Subscription) -> Void)?, receiveOutput: ((Self.Output) -> Void)?, receiveCompletion: ((Subscribers.Completion<Self.Failure>) -> Void)?, receiveCancel: (() -> Void)?, receiveRequest: ((Subscribers.Demand) -> Void)?) -> Publishers.HandleEvents<Self>](loadrequest/handleevents(receivesubscription:receiveoutput:receivecompletion:receivecancel:receiverequest:).md)
  Performs the specified closures when publisher events occur.
- [func print(String, to: (any TextOutputStream)?) -> Publishers.Print<Self>](loadrequest/print(_:to:).md)
  Prints log messages for all publishing events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/loadrequest/breakpoint(receivesubscription:receiveoutput:receivecompletion:))*