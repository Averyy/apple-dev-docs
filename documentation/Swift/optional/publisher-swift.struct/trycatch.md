# tryCatch(_:)

**Framework**: Swift  
**Kind**: method

Handles errors from an upstream publisher by either replacing it with another publisher or throwing a new error.

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
func tryCatch<P>(_ handler: @escaping (Self.Failure) throws -> P) -> Publishers.TryCatch<Self, P> where P : Publisher, Self.Output == P.Output
```

#### Return Value

A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher, or an error.

#### Discussion

Use [`tryCatch(_:)`](optional/publisher-swift.struct/trycatch(_:).md) to decide how to handle from an upstream publisher by either replacing the publisher with a new publisher, or throwing a new error.

In the example below, an array publisher emits values that a [`tryMap(_:)`](optional/publisher-swift.struct/trymap(_:).md) operator evaluates to ensure the values are greater than zero. If the values aren’t greater than zero, the operator throws an error to the downstream subscriber to let it know there was a problem. The subscriber, [`tryCatch(_:)`](optional/publisher-swift.struct/trycatch(_:).md), replaces the error with a new publisher using `Just` to publish a final value before the stream ends normally.

```swift
enum SimpleError: Error { case error }
var numbers = [5, 4, 3, 2, 1, -1, 7, 8, 9, 10]

cancellable = numbers.publisher
   .tryMap { v in
        if v > 0 {
            return v
        } else {
            throw SimpleError.error
        }
}
  .tryCatch { error in
      Just(0) // Send a final value before completing normally.
              // Alternatively, throw a new error to terminate the stream.
}
  .sink(receiveCompletion: { print ("Completion: \($0).") },
        receiveValue: { print ("Received \($0).") }
  )
//    Received 5.
//    Received 4.
//    Received 3.
//    Received 2.
//    Received 1.
//    Received 0.
//    Completion: finished.
```

## Parameters

- `handler`: A throwing closure that accepts the upstream failure as input. This closure can either replace the upstream publisher with a new one, or throw a new error to the downstream subscriber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/publisher-swift.struct/trycatch(_:))*