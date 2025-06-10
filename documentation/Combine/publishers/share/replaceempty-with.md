# replaceEmpty(with:)

**Framework**: Combine  
**Kind**: method

Replaces an empty stream with the provided element.

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
func replaceEmpty(with output: Self.Output) -> Publishers.ReplaceEmpty<Self>
```

#### Return Value

A publisher that replaces an empty stream with the provided output element.

#### Discussion

Use [`replaceEmpty(with:)`](publisher/replaceempty(with:).md) to provide a replacement element if the upstream publisher finishes without producing any elements.

In the example below, the empty `Double` array publisher doesn’t produce any elements, so [`replaceEmpty(with:)`](publisher/replaceempty(with:).md) publishes `Double.nan` and finishes normally.

```swift
let numbers: [Double] = []
cancellable = numbers.publisher
    .replaceEmpty(with: Double.nan)
    .sink { print("\($0)", terminator: " ") }

// Prints "(nan)".
```

Conversely, providing a non-empty publisher publishes all elements and the publisher then terminates normally:

```swift
let otherNumbers: [Double] = [1.0, 2.0, 3.0]
cancellable2 = otherNumbers.publisher
    .replaceEmpty(with: Double.nan)
    .sink { print("\($0)", terminator: " ") }

// Prints: 1.0 2.0 3.0
```

## Parameters

- `output`: An element to emit when the upstream publisher finishes without emitting any elements.

## See Also

- [func filter((Self.Output) -> Bool) -> Publishers.Filter<Self>](publishers/share/filter(_:).md)
  Republishes all elements that match a provided closure.
- [func tryFilter((Self.Output) throws -> Bool) -> Publishers.TryFilter<Self>](publishers/share/tryfilter(_:).md)
  Republishes all elements that match a provided error-throwing closure.
- [func compactMap<T>((Self.Output) -> T?) -> Publishers.CompactMap<Self, T>](publishers/share/compactmap(_:).md)
  Calls a closure with each received element and publishes any returned optional that has a value.
- [func tryCompactMap<T>((Self.Output) throws -> T?) -> Publishers.TryCompactMap<Self, T>](publishers/share/trycompactmap(_:).md)
  Calls an error-throwing closure with each received element and publishes any returned optional that has a value.
- [func removeDuplicates() -> Publishers.RemoveDuplicates<Self>](publishers/share/removeduplicates.md)
  Publishes only elements that don’t match the previous element.
- [func removeDuplicates(by: (Self.Output, Self.Output) -> Bool) -> Publishers.RemoveDuplicates<Self>](publishers/share/removeduplicates(by:).md)
  Publishes only elements that don’t match the previous element, as evaluated by a provided closure.
- [func tryRemoveDuplicates(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryRemoveDuplicates<Self>](publishers/share/tryremoveduplicates(by:).md)
  Publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [func replaceError(with: Self.Output) -> Publishers.ReplaceError<Self>](publishers/share/replaceerror(with:).md)
  Replaces any errors in the stream with the provided element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/share/replaceempty(with:))*