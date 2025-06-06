# tryCompactMap(_:)

**Framework**: RealityKit  
**Kind**: method

Calls an error-throwing closure with each received element and publishes any returned optional that has a value.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
func tryCompactMap<T>(_ transform: @escaping (Self.Output) throws -> T?) -> Publishers.TryCompactMap<Self, T>
```

#### Return Value

Any non-`nil` optional results of calling the supplied closure.

#### Discussion

Use `Publisher/tryCompactMap(_:)` to remove `nil` elements from a publisher’s stream based on an error-throwing closure you provide. If the closure throws an error, the publisher cancels the upstream publisher and sends the thrown error to the downstream subscriber as a `Publisher/Failure`.

The following example uses an array of numbers as the source for a collection-based publisher. A `Publisher/tryCompactMap(_:)` operator consumes each integer from the publisher and uses a dictionary to transform the numbers from its Arabic to Roman numerals, as an optional [`String`](https://developer.apple.com/documentation/Swift/String).

If the closure called by `Publisher/tryCompactMap(_:)` fails to look up a Roman numeral, it returns the optional String `(unknown)`.

If the closure called by `Publisher/tryCompactMap(_:)` determines the input is `0`, it throws an error. The `Publisher/tryCompactMap(_:)` operator catches this error and stops publishing, sending a `Subscribers/Completion/failure(_:)` that wraps the error.

```None
struct ParseError: Error {}
func romanNumeral(from: Int) throws -> String? {
    let romanNumeralDict: [Int : String] =
        [1: "I", 2: "II", 3: "III", 4: "IV", 5: "V"]
    guard from != 0 else { throw ParseError() }
    return romanNumeralDict[from]
}
let numbers = [6, 5, 4, 3, 2, 1, 0]
cancellable = numbers.publisher
    .tryCompactMap { try romanNumeral(from: $0) }
    .sink(
          receiveCompletion: { print ("\($0)") },
          receiveValue: { print ("\($0)", terminator: " ") }
     )

// Prints: "(Unknown) V IV III II I failure(ParseError())"
```

## Parameters

- `transform`: An error-throwing closure that receives a value and returns an optional value.

## See Also

- [func filter((Self.Output) -> Bool) -> Publishers.Filter<Self>](loadrequest/filter(_:).md)
  Republishes all elements that match a provided closure.
- [func tryFilter((Self.Output) throws -> Bool) -> Publishers.TryFilter<Self>](loadrequest/tryfilter(_:).md)
  Republishes all elements that match a provided error-throwing closure.
- [func compactMap<T>((Self.Output) -> T?) -> Publishers.CompactMap<Self, T>](loadrequest/compactmap(_:).md)
  Calls a closure with each received element and publishes any returned optional that has a value.
- [func removeDuplicates() -> Publishers.RemoveDuplicates<Self>](loadrequest/removeduplicates.md)
  Publishes only elements that don’t match the previous element.
- [func removeDuplicates(by: (Self.Output, Self.Output) -> Bool) -> Publishers.RemoveDuplicates<Self>](loadrequest/removeduplicates(by:).md)
  Publishes only elements that don’t match the previous element, as evaluated by a provided closure.
- [func tryRemoveDuplicates(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryRemoveDuplicates<Self>](loadrequest/tryremoveduplicates(by:).md)
  Publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [func replaceEmpty(with: Self.Output) -> Publishers.ReplaceEmpty<Self>](loadrequest/replaceempty(with:).md)
  Replaces an empty stream with the provided element.
- [func replaceError(with: Self.Output) -> Publishers.ReplaceError<Self>](loadrequest/replaceerror(with:).md)
  Replaces any errors in the stream with the provided element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/loadrequest/trycompactmap(_:))*