# tryFilter(_:)

**Framework**: Combine  
**Kind**: method

Republishes all elements that match a provided error-throwing closure.

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
func tryFilter(_ isIncluded: @escaping (Self.Output) throws -> Bool) -> Publishers.TryFilter<Self>
```

#### Return Value

A publisher that republishes all elements that satisfy the closure.

#### Discussion

Use [`tryFilter(_:)`](publisher/tryfilter(_:).md) to filter elements evaluated in an error-throwing closure. If the `isIncluded` closure throws an error, the publisher fails with that error.

In the example below, [`tryFilter(_:)`](publisher/tryfilter(_:).md) checks to see if the element provided by the publisher is zero, and throws a `ZeroError` before terminating the publisher with the thrown error. Otherwise, it republishes the element only if it’s even:

```swift
struct ZeroError: Error {}

let numbers: [Int] = [1, 2, 3, 4, 0, 5]
cancellable = numbers.publisher
    .tryFilter{
        if $0 == 0 {
            throw ZeroError()
        } else {
            return $0 % 2 == 0
        }
    }
    .sink(
        receiveCompletion: { print ("\($0)") },
        receiveValue: { print ("\($0)", terminator: " ") }
     )

// Prints: "2 4 failure(DivisionByZeroError())".
```

## Parameters

- `isIncluded`: A closure that takes one element and returns a Boolean value that indicated whether to republish the element or throws an error.

## See Also

- [func filter((Self.Output) -> Bool) -> Publishers.Filter<Self>](publishers/switchtolatest/filter(_:).md)
  Republishes all elements that match a provided closure.
- [func compactMap<T>((Self.Output) -> T?) -> Publishers.CompactMap<Self, T>](publishers/switchtolatest/compactmap(_:).md)
  Calls a closure with each received element and publishes any returned optional that has a value.
- [func tryCompactMap<T>((Self.Output) throws -> T?) -> Publishers.TryCompactMap<Self, T>](publishers/switchtolatest/trycompactmap(_:).md)
  Calls an error-throwing closure with each received element and publishes any returned optional that has a value.
- [func removeDuplicates() -> Publishers.RemoveDuplicates<Self>](publishers/switchtolatest/removeduplicates.md)
  Publishes only elements that don’t match the previous element.
- [func removeDuplicates(by: (Self.Output, Self.Output) -> Bool) -> Publishers.RemoveDuplicates<Self>](publishers/switchtolatest/removeduplicates(by:).md)
  Publishes only elements that don’t match the previous element, as evaluated by a provided closure.
- [func tryRemoveDuplicates(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryRemoveDuplicates<Self>](publishers/switchtolatest/tryremoveduplicates(by:).md)
  Publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [func replaceEmpty(with: Self.Output) -> Publishers.ReplaceEmpty<Self>](publishers/switchtolatest/replaceempty(with:).md)
  Replaces an empty stream with the provided element.
- [func replaceError(with: Self.Output) -> Publishers.ReplaceError<Self>](publishers/switchtolatest/replaceerror(with:).md)
  Replaces any errors in the stream with the provided element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/switchtolatest/tryfilter(_:))*