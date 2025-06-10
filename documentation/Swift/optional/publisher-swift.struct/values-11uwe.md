# values

**Framework**: Swift  
**Kind**: property

The elements produced by the publisher, as an asynchronous sequence.

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
var values: AsyncPublisher<Self> { get }
```

#### Discussion

This property provides an `AsyncPublisher`, which allows you to use the Swift `async`-`await` syntax to receive the publisher’s elements. Because `AsyncPublisher` conforms to [`AsyncSequence`](AsyncSequence.md), you iterate over its elements with a `for`-`await`-`in` loop, rather than attaching a subscriber.

The following example shows how to use the `values` property to receive elements asynchronously. The example adapts a code snippet from the [`filter(_:)`](optional/publisher-swift.struct/filter(_:).md) operator’s documentation, which filters a sequence to only emit even integers. This example replaces the `Subscribers/Sink` subscriber with a `for`-`await`-`in` loop that iterates over the `AsyncPublisher` provided by the `values` property.

```swift
let numbers: [Int] = [1, 2, 3, 4, 5]
let filtered = numbers.publisher
    .filter { $0 % 2 == 0 }

for await number in filtered.values
{
    print("\(number)", terminator: " ")
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/publisher-swift.struct/values-11uwe)*