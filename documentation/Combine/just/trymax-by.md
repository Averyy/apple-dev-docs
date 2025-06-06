# tryMax(by:)

**Framework**: Combine  
**Kind**: method

Publishes the maximum value received from the upstream publisher, using the provided error-throwing closure to order the items.

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
func tryMax(by areInIncreasingOrder: @escaping (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryComparison<Self>
```

#### Return Value

A publisher that publishes the maximum value received from the upstream publisher, after the upstream publisher finishes.

#### Discussion

Use [`tryMax(by:)`](publisher/trymax(by:).md) to determine the maximum value of elements received from the upstream publisher using an error-throwing closure you specify.

In the example below, an array publishes elements. The [`tryMax(by:)`](publisher/trymax(by:).md) operator executes the error-throwing closure that throws when the `first` element is an odd number, terminating the publisher.

```swift
struct IllegalValueError: Error {}

let numbers: [Int]  = [0, 10, 6, 13, 22, 22]
cancellable = numbers.publisher
    .tryMax { first, second -> Bool in
        if (first % 2 != 0) {
            throw IllegalValueError()
        }
        return first > second
    }
    .sink(
        receiveCompletion: { print ("completion: \($0)") },
        receiveValue: { print ("value: \($0)") }
    )

// Prints: completion: failure(IllegalValueError())
```

After this publisher receives a request for more than 0 items, it requests unlimited items from its upstream publisher.

## Parameters

- `areInIncreasingOrder`: A throwing closure that receives two elements and returns   if they’re in increasing order. If this closure throws, the publisher terminates with a  .

## See Also

- [func count() -> Just<Int>](just/count.md)
- [func max() -> Just<Output>](just/max.md)
- [func max(by: (Output, Output) -> Bool) -> Just<Output>](just/max(by:).md)
- [func min() -> Just<Output>](just/min.md)
- [func min(by: (Output, Output) -> Bool) -> Just<Output>](just/min(by:).md)
- [func tryMin(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryComparison<Self>](just/trymin(by:).md)
  Publishes the minimum value received from the upstream publisher, using the provided error-throwing closure to order the items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/trymax(by:))*