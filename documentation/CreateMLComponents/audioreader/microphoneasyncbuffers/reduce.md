# reduce(_:_:)

**Framework**: Create ML Components  
**Kind**: method

Returns the result of combining the elements of the asynchronous sequence using the given closure.

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
func reduce<Result>(_ initialResult: Result, _ nextPartialResult: (Result, Self.Element) async throws -> Result) async rethrows -> Result
```

#### Return Value

The final accumulated value. If the sequence has no elements, the result is `initialResult`.

#### Discussion

Use the `reduce(_:_:)` method to produce a single value from the elements of an entire sequence. For example, you can use this method on an sequence of numbers to find their sum or product.

The `nextPartialResult` closure executes sequentially with an accumulating value initialized to `initialResult` and each element of the sequence.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `4`. The `reduce(_:_:)` method sums the values received from the asynchronous sequence.

```None
let sum = await Counter(howHigh: 4)
    .reduce(0) {
        $0 + $1
    }
print(sum)
// Prints "10"
```

## Parameters

- `initialResult`: The value to use as the initial accumulating value.   The   closure receives   the first   time the closure runs.
- `nextPartialResult`: A closure that combines an accumulating value and   an element of the asynchronous sequence into a new accumulating value,   for use in the next call of the   closure or   returned to the caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audioreader/microphoneasyncbuffers/reduce(_:_:))*