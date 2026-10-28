# sink(receiveValue:)

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

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

Available when `Failure` is `Never`.

## Mentions

- [Processing Published Elements with Subscribers](../processing-published-elements-with-subscribers.md)
- [Using Combine for Your App’s Asynchronous Code](../using-combine-for-your-app-s-asynchronous-code.md)
- [Controlling Publishing with Connectable Publishers](../controlling-publishing-with-connectable-publishers.md)
- [Replacing Foundation Timers with Timer Publishers](../replacing-foundation-timers-with-timer-publishers.md)

## Return Value

A cancellable instance, which you use when you end assignment of the received value. Deallocation of the result will tear down the subscription stream.

## Discussion

Use [`sink(receiveValue:)`](./sink%28receivevalue%29.md) to observe values received by the publisher and print them to the console. This operator can only be used when the stream doesn’t fail, that is, when the publisher’s [`Failure`](./failure.md) type is [`Never`](../../Swift/never.md).

In this example, a [`Range`](../../Swift/range.md) publisher publishes integers to a [`sink(receiveValue:)`](./sink%28receivevalue%29.md) operator’s `receiveValue` closure that prints them to the console:

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

### Connecting simple subscribers
- [func assign<Root>(to: ReferenceWritableKeyPath<Root, Self.Output>, on: Root) -> AnyCancellable](./assign%28to,on%29.md)
  Assigns each element from a publisher to a property on an object.
- [func assign(to: inout Published<Self.Output>.Publisher)](./assign%28to%29.md)
  Republishes elements received from a publisher, by assigning them to a property marked as a publisher.
- [func sink(receiveCompletion: (Subscribers.Completion<Self.Failure>) -> Void, receiveValue: (Self.Output) -> Void) -> AnyCancellable](./sink%28receivecompletion,receivevalue%29.md)
  Attaches a subscriber with closure-based behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publisher/sink(receivevalue:))*