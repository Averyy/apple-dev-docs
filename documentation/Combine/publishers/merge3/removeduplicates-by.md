# removeDuplicates(by:)

**Framework**: Combine  
**Kind**: method

Publishes only elements that don’t match the previous element, as evaluated by a provided closure.

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
func removeDuplicates(by predicate: @escaping (Self.Output, Self.Output) -> Bool) -> Publishers.RemoveDuplicates<Self>
```

#### Return Value

A publisher that consumes — rather than publishes — duplicate elements.

#### Discussion

Use [`removeDuplicates(by:)`](publisher/removeduplicates(by:).md) to remove repeating elements from an upstream publisher based upon the evaluation of the current and previously published elements using a closure you provide.

Use the [`removeDuplicates(by:)`](publisher/removeduplicates(by:).md) operator when comparing types that don’t themselves implement `Equatable`, or if you need to compare values differently than the type’s `Equatable` implementation.

In the example below, the [`removeDuplicates(by:)`](publisher/removeduplicates(by:).md) functionality triggers when the `x` property of the current and previous elements are equal, otherwise the operator publishes the current `Point` to the downstream subscriber:

```swift
struct Point {
    let x: Int
    let y: Int
}

let points = [Point(x: 0, y: 0), Point(x: 0, y: 1),
              Point(x: 1, y: 1), Point(x: 2, y: 1)]
cancellable = points.publisher
    .removeDuplicates { prev, current in
        // Considers points to be duplicate if the x coordinate
        // is equal, and ignores the y coordinate
        prev.x == current.x
    }
    .sink { print("\($0)", terminator: " ") }

// Prints: Point(x: 0, y: 0) Point(x: 1, y: 1) Point(x: 2, y: 1)
```

## Parameters

- `predicate`: A closure to evaluate whether two elements are equivalent, for purposes of filtering. Return   from this closure to indicate that the second element is a duplicate of the first.

## See Also

- [func filter((Self.Output) -> Bool) -> Publishers.Filter<Self>](publishers/merge3/filter(_:).md)
  Republishes all elements that match a provided closure.
- [func tryFilter((Self.Output) throws -> Bool) -> Publishers.TryFilter<Self>](publishers/merge3/tryfilter(_:).md)
  Republishes all elements that match a provided error-throwing closure.
- [func compactMap<T>((Self.Output) -> T?) -> Publishers.CompactMap<Self, T>](publishers/merge3/compactmap(_:).md)
  Calls a closure with each received element and publishes any returned optional that has a value.
- [func tryCompactMap<T>((Self.Output) throws -> T?) -> Publishers.TryCompactMap<Self, T>](publishers/merge3/trycompactmap(_:).md)
  Calls an error-throwing closure with each received element and publishes any returned optional that has a value.
- [func removeDuplicates() -> Publishers.RemoveDuplicates<Self>](publishers/merge3/removeduplicates.md)
  Publishes only elements that don’t match the previous element.
- [func tryRemoveDuplicates(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryRemoveDuplicates<Self>](publishers/merge3/tryremoveduplicates(by:).md)
  Publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [func replaceEmpty(with: Self.Output) -> Publishers.ReplaceEmpty<Self>](publishers/merge3/replaceempty(with:).md)
  Replaces an empty stream with the provided element.
- [func replaceError(with: Self.Output) -> Publishers.ReplaceError<Self>](publishers/merge3/replaceerror(with:).md)
  Replaces any errors in the stream with the provided element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/merge3/removeduplicates(by:))*