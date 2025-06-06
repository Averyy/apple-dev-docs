# sink(receiveValue:)

**Framework**: RealityKit  
**Kind**: method

Attaches a subscriber with closure-based behavior to a publisher that never fails.

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
func sink(receiveValue: @escaping (Self.Output) -> Void) -> AnyCancellable
```

#### Return Value

A cancellable instance, which you use when you end assignment of the received value. Deallocation of the result will tear down the subscription stream.

#### Discussion

Use [`sink(receiveValue:)`](scene/publisher/sink(receivevalue:).md) to observe values received by the publisher and print them to the console. This operator can only be used when the stream doesn’t fail, that is, when the publisher’s [`Scene.Publisher.Failure`](scene/publisher/failure.md) type is [`Never`](https://developer.apple.com/documentation/Swift/Never).

In this example, a [`Range`](https://developer.apple.com/documentation/Swift/Range) publisher publishes integers to a [`sink(receiveValue:)`](scene/publisher/sink(receivevalue:).md) operator’s `receiveValue` closure that prints them to the console:

```None
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

- [func assign<Root>(to: ReferenceWritableKeyPath<Root, Self.Output>, on: Root) -> AnyCancellable](scene/publisher/assign(to:on:).md)
  Assigns each element from a publisher to a property on an object.
- [func sink(receiveCompletion: (Subscribers.Completion<Self.Failure>) -> Void, receiveValue: (Self.Output) -> Void) -> AnyCancellable](scene/publisher/sink(receivecompletion:receivevalue:).md)
  Attaches a subscriber with closure-based behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/publisher/sink(receivevalue:))*