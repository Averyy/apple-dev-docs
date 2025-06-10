# sink(receiveCompletion:receiveValue:)

**Framework**: Combine  
**Kind**: method

Attaches a subscriber with closure-based behavior.

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
func sink(receiveCompletion: @escaping (Subscribers.Completion<Self.Failure>) -> Void, receiveValue: @escaping (Self.Output) -> Void) -> AnyCancellable
```

#### Return Value

A cancellable instance, which you use when you end assignment of the received value. Deallocation of the result will tear down the subscription stream.

#### Discussion

Use [`sink(receiveCompletion:receiveValue:)`](publisher/sink(receivecompletion:receivevalue:).md) to observe values received by the publisher and process them using a closure you specify.

In this example, a [`Range`](https://developer.apple.com/documentation/Swift/Range) publisher publishes integers to a [`sink(receiveCompletion:receiveValue:)`](publisher/sink(receivecompletion:receivevalue:).md) operator’s `receiveValue` closure that prints them to the console. Upon completion the [`sink(receiveCompletion:receiveValue:)`](publisher/sink(receivecompletion:receivevalue:).md) operator’s `receiveCompletion` closure indicates the successful termination of the stream.

```swift
let myRange = (0...3)
cancellable = myRange.publisher
    .sink(receiveCompletion: { print ("completion: \($0)") },
          receiveValue: { print ("value: \($0)") })

// Prints:
//  value: 0
//  value: 1
//  value: 2
//  value: 3
//  completion: finished
```

This method creates the subscriber and immediately requests an unlimited number of values, prior to returning the subscriber. The return value should be held, otherwise the stream will be canceled.

## Parameters

- `receiveValue`: The closure to execute on receipt of a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/tryallsatisfy/sink(receivecompletion:receivevalue:))*