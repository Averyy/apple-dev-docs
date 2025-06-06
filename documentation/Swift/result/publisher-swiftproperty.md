# publisher

**Framework**: Swift  
**Kind**: property

A Combine publisher that publishes this instance’s result to each subscriber exactly once, or fails immediately if the result indicates failure.

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
var publisher: Result<Success, Failure>.Publisher { get }
```

#### Discussion

In the following example, `goodResult` provides a successful result with the integer value `1`. A sink subscriber connected to the result’s publisher receives the output `1`, followed by a normal completion ([`Subscribers.Completion.finished`](https://developer.apple.com/documentation/Combine/Subscribers/Completion/finished)).

```swift
 let goodResult: Result<Int, MyError> = .success(1)
 goodResult.publisher
     .sink(receiveCompletion: { print("goodResult done: \($0)")},
           receiveValue: { print("goodResult value: \($0)")} )
 // Prints:
 // goodResult value: 1
 // goodResult done: finished
```

In contrast with the [`Just`](https://developer.apple.com/documentation/Combine/Just) publisher, which always publishes a single value, this publisher might not send any values and instead terminate with an error, if the result is `/Swift/Result/failure`. In the next example, `badResult` is a failure result that wraps a custom error. A sink subscriber connected to this result’s publisher immediately receives a termination ([`Subscribers.Completion.failure(_:)`](https://developer.apple.com/documentation/Combine/Subscribers/Completion/failure(_:))).

```swift
 struct MyError: Error, CustomDebugStringConvertible {
     var debugDescription: String = "MyError"
 }
 let badResult: Result<Int, MyError> = .failure(MyError())
 badResult.publisher
     .sink(receiveCompletion: { print("badResult done: \($0)")},
           receiveValue: { print("badResult value: \($0)")} )
 // Prints:
 // badResult done: failure(MyError)
```

## See Also

- [Result.Publisher](result/publisher-swift.struct.md)
  The type of a Combine publisher that publishes this instance’s result to each subscriber exactly once, or fails immediately if the result indicates failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/publisher-swift.property)*