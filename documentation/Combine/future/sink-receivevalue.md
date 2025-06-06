# sink(receiveValue:)

**Framework**: Combine  
**Kind**: method

Attaches a subscriber with closure-based behavior to a publisher that never fails.

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
func sink(receiveValue: @escaping (Self.Output) -> Void) -> AnyCancellable
```

#### Return Value

A cancellable instance, which you use when you end assignment of the received value. Deallocation of the result will tear down the subscription stream.

#### Discussion

Use [`sink(receiveValue:)`](publisher/sink(receivevalue:).md) to observe values received by the publisher and print them to the console. This operator can only be used when the stream doesn’t fail, that is, when the publisher’s [`Failure`](publisher/failure.md) type is [`Never`](https://developer.apple.com/documentation/Swift/Never).

In this example, a [`Range`](https://developer.apple.com/documentation/Swift/Range) publisher publishes integers to a [`sink(receiveValue:)`](publisher/sink(receivevalue:).md) operator’s `receiveValue` closure that prints them to the console:

```swift
let integers = (0...3)
integers.publisher
    .sink { print("Received \($0)") }

// Prints:
//  Received 0
//  Received 1
//  Received 2
//  Received 3
```

This method creates the subscriber and immediately requests an unlimited number of values, prior to returning the subscriber. The return value should be held, otherwise the stream will be canceled.

## Parameters

- `receiveValue`: The closure to execute on receipt of a value.

## See Also

- [func assign<Root>(to: ReferenceWritableKeyPath<Root, Self.Output>, on: Root) -> AnyCancellable](future/assign(to:on:).md)
  Assigns each element from a publisher to a property on an object.
- [func assign(to: inout Published<Self.Output>.Publisher)](future/assign(to:).md)
  Republishes elements received from a publisher, by assigning them to a property marked as a publisher.
- [func sink(receiveCompletion: (Subscribers.Completion<Self.Failure>) -> Void, receiveValue: (Self.Output) -> Void) -> AnyCancellable](future/sink(receivecompletion:receivevalue:).md)
  Attaches a subscriber with closure-based behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/future/sink(receivevalue:))*