# tryDrop(while:)

**Framework**: Swift  
**Kind**: method

Omits elements from the upstream publisher until an error-throwing closure returns false, before republishing all remaining elements.

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
func tryDrop(while predicate: @escaping (Self.Output) throws -> Bool) -> Publishers.TryDropWhile<Self>
```

#### Return Value

A publisher that skips over elements until the provided closure returns `false`, and then republishes all remaining elements. If the predicate closure throws, the publisher fails with an error.

#### Discussion

Use [`tryDrop(while:)`](optional/publisher-swift.struct/trydrop(while:).md) to omit elements from an upstream until an error-throwing closure you provide returns false, after which the remaining items in the stream are published. If the closure throws, no elements are emitted and the publisher fails with an error.

In the example below, elements are ignored until `-1` is encountered in the stream and the closure returns `false`. The publisher then republishes the remaining elements and finishes normally. Conversely, if the `guard` value in the closure had been encountered, the closure would throw and the publisher would fail with an error.

```swift
struct RangeError: Error {}
var numbers = [1, 2, 3, 4, 5, 6, -1, 7, 8, 9, 10]
let range: CountableClosedRange<Int> = (1...100)
cancellable = numbers.publisher
    .tryDrop {
        guard $0 != 0 else { throw RangeError() }
        return range.contains($0)
    }
    .sink(
        receiveCompletion: { print ("completion: \($0)") },
        receiveValue: { print ("value: \($0)") }
    )

// Prints: "-1 7 8 9 10 completion: finished"
// If instead numbers was [1, 2, 3, 4, 5, 6, 0, -1, 7, 8, 9, 10], tryDrop(while:) would fail with a RangeError.
```

## Parameters

- `predicate`: A closure that takes an element as a parameter and returns a Boolean value indicating whether to drop the element from the publisher’s output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/publisher-swift.struct/trydrop(while:))*