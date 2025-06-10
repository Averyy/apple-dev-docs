# breakpointOnError()

**Framework**: Combine  
**Kind**: method

Raises a debugger signal upon receiving a failure.

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
func breakpointOnError() -> Publishers.Breakpoint<Self>
```

#### Return Value

A publisher that raises a debugger signal upon receiving a failure.

#### Discussion

When the upstream publisher fails with an error, this publisher raises the `SIGTRAP` signal, which stops the process in the debugger. Otherwise, this publisher passes through values and completions as-is.

In this example a [`PassthroughSubject`](passthroughsubject.md) publishes strings, but its downstream [`tryMap(_:)`](publisher/trymap(_:).md) operator throws an error. This sends the error downstream as a [`Subscribers.Completion.failure(_:)`](subscribers/completion/failure(_:).md). The [`breakpointOnError()`](publisher/breakpointonerror().md) operator receives this completion and stops the app in the debugger.

```swift
 struct CustomError : Error {}
 let publisher = PassthroughSubject<String?, Error>()
 cancellable = publisher
     .tryMap { stringValue in
         throw CustomError()
     }
     .breakpointOnError()
     .sink(
         receiveCompletion: { completion in print("Completion: \(String(describing: completion))") },
         receiveValue: { aValue in print("Result: \(String(describing: aValue))") }
     )

 publisher.send("TEST DATA")

 // Prints: "error: Execution was interrupted, reason: signal SIGTRAP."
 // Depending on your specific environment, the console messages may
 // also include stack trace information, which is not shown here.
```

## See Also

- [func breakpoint(receiveSubscription: ((any Subscription) -> Bool)?, receiveOutput: ((Self.Output) -> Bool)?, receiveCompletion: ((Subscribers.Completion<Self.Failure>) -> Bool)?) -> Publishers.Breakpoint<Self>](publishers/subscribeon/breakpoint(receivesubscription:receiveoutput:receivecompletion:).md)
  Raises a debugger signal when a provided closure needs to stop the process in the debugger.
- [func handleEvents(receiveSubscription: ((any Subscription) -> Void)?, receiveOutput: ((Self.Output) -> Void)?, receiveCompletion: ((Subscribers.Completion<Self.Failure>) -> Void)?, receiveCancel: (() -> Void)?, receiveRequest: ((Subscribers.Demand) -> Void)?) -> Publishers.HandleEvents<Self>](publishers/subscribeon/handleevents(receivesubscription:receiveoutput:receivecompletion:receivecancel:receiverequest:).md)
  Performs the specified closures when publisher events occur.
- [func print(String, to: (any TextOutputStream)?) -> Publishers.Print<Self>](publishers/subscribeon/print(_:to:).md)
  Prints log messages for all publishing events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/subscribeon/breakpointonerror())*