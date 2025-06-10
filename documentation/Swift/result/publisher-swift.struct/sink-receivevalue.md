# sink(receiveValue:)

**Framework**: Swift  
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

Use [`sink(receiveValue:)`](result/publisher-swift.struct/sink(receivevalue:).md) to observe values received by the publisher and print them to the console. This operator can only be used when the stream doesn’t fail, that is, when the publisher’s `Publisher/Failure` type is [`Never`](Never.md).

In this example, a [`Range`](Range.md) publisher publishes integers to a [`sink(receiveValue:)`](result/publisher-swift.struct/sink(receivevalue:).md) operator’s `receiveValue` closure that prints them to the console:

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/publisher-swift.struct/sink(receivevalue:))*