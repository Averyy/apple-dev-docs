# output(in:)

**Framework**: Combine  
**Kind**: method

Publishes elements specified by their range in the sequence of published elements.

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
func output<R>(in range: R) -> Publishers.Output<Self> where R : RangeExpression, R.Bound == Int
```

#### Return Value

A publisher that publishes elements specified by a range.

#### Discussion

Use [`output(in:)`](publisher/output(in:).md) to republish a range indices you specify in the published stream. After publishing all elements, the publisher finishes normally. If the publisher completes normally or with an error before producing all the elements in the range, it doesn’t publish the remaining elements.

In the example below, an array publisher emits the subset of elements at the indices in the specified range:

```swift
let numbers = [1, 1, 2, 2, 2, 3, 4, 5, 6]
numbers.publisher
    .output(in: (3...5))
    .sink { print("\($0)", terminator: " ") }

// Prints: "2 2 3"
```

## Parameters

- `range`: A range that indicates which elements to publish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/output(in:)-36ht0)*