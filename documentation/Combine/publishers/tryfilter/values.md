# values

**Framework**: Combine  
**Kind**: property

The elements produced by the publisher, as a throwing asynchronous sequence.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var values: AsyncThrowingPublisher<Self> { get }
```

#### Discussion

This property provides an [`AsyncThrowingPublisher`](asyncthrowingpublisher.md), which allows you to use the Swift `async`-`await` syntax to receive the publisher’s elements. Because [`AsyncPublisher`](asyncpublisher.md) conforms to [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence), you iterate over its elements with a `for`-`await`-`in` loop, rather than attaching a subscriber. If the publisher terminates with an error, the awaiting caller receives the error as a `throw`.

The following example shows how to use the `values` property to receive elements asynchronously. The example adapts a code snippet from the [`tryFilter(_:)`](publisher/tryfilter(_:).md) operator’s documentation, which filters a sequence to only emit even integers, and terminate with an error on a `0`. This example replaces the [`Subscribers.Sink`](subscribers/sink.md) subscriber with a `for`-`await`-`in` loop that iterates over the [`AsyncPublisher`](asyncpublisher.md) provided by the `values` property. With this approach, the error handling previously provided in the sink subscriber’s [`receiveCompletion`](subscribers/sink/receivecompletion.md) closure goes instead in a `catch` block.

```swift
let numbers: [Int] = [1, 2, 3, 4, 0, 5]
let filterPublisher = numbers.publisher
    .tryFilter{
        if $0 == 0 {
            throw ZeroError()
        } else {
            return $0 % 2 == 0
        }
    }

do {
    for try await number in filterPublisher.values {
        print ("\(number)", terminator: " ")
    }
} catch {
    print ("\(error)")
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/tryfilter/values)*