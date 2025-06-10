# reduce(_:_:)

**Framework**: TabularData  
**Kind**: method

Returns the result of combining the elements of the sequence using the given closure.

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
func reduce<Result>(_ initialResult: Result, _ nextPartialResult: (Result, Self.Element) throws -> Result) rethrows -> Result
```

#### Return Value

The final accumulated value. If the sequence has no elements, the result is `initialResult`.

#### Discussion

Use the `reduce(_:_:)` method to produce a single value from the elements of an entire sequence. For example, you can use this method on an array of numbers to find their sum or product.

The `nextPartialResult` closure is called sequentially with an accumulating value initialized to `initialResult` and each element of the sequence. This example shows how to find the sum of an array of numbers.

```None
let numbers = [1, 2, 3, 4]
let numberSum = numbers.reduce(0, { x, y in
    x + y
})
// numberSum == 10
```

When `numbers.reduce(_:_:)` is called, the following steps occur:

1. The `nextPartialResult` closure is called with `initialResult`—`0` in this case—and the first element of `numbers`, returning the sum: `1`.
2. The closure is called again repeatedly with the previous call’s return value and each element of the sequence.
3. When the sequence is exhausted, the last value returned from the closure is returned to the caller.

If the sequence has no elements, `nextPartialResult` is never executed and `initialResult` is the result of the call to `reduce(_:_:)`.

> **Note**: O(), where  is the length of the sequence.

## Parameters

- `initialResult`: The value to use as the initial accumulating value.    is passed to   the first time the   closure is executed.
- `nextPartialResult`: A closure that combines an accumulating value and   an element of the sequence into a new accumulating value, to be used   in the next call of the   closure or returned to   the caller.

## See Also

- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](rowgrouping/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgrouping/reduce(_:_:))*