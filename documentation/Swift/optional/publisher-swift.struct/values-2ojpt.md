# values

**Framework**: Swift  
**Kind**: property

The elements produced by the publisher, as a throwing asynchronous sequence.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
var values: AsyncThrowingPublisher<Self> { get }
```

#### Discussion

This property provides an `AsyncThrowingPublisher`, which allows you to use the Swift `async`-`await` syntax to receive the publisher’s elements. Because `AsyncPublisher` conforms to [`AsyncSequence`](AsyncSequence.md), you iterate over its elements with a `for`-`await`-`in` loop, rather than attaching a subscriber. If the publisher terminates with an error, the awaiting caller receives the error as a `throw`.

The following example shows how to use the `values` property to receive elements asynchronously. The example adapts a code snippet from the [`tryFilter(_:)`](optional/publisher-swift.struct/tryfilter(_:).md) operator’s documentation, which filters a sequence to only emit even integers, and terminate with an error on a `0`. This example replaces the `Subscribers/Sink` subscriber with a `for`-`await`-`in` loop that iterates over the `AsyncPublisher` provided by the `values` property. With this approach, the error handling previously provided in the sink subscriber’s `Subscribers/Sink/receiveCompletion` closure goes instead in a `catch` block.

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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/publisher-swift.struct/values-2ojpt)*