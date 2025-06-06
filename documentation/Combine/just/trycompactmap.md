# tryCompactMap(_:)

**Framework**: Combine  
**Kind**: method

Calls an error-throwing closure with each received element and publishes any returned optional that has a value.

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
func tryCompactMap<T>(_ transform: @escaping (Self.Output) throws -> T?) -> Publishers.TryCompactMap<Self, T>
```

#### Return Value

Any non-`nil` optional results of calling the supplied closure.

#### Discussion

Use [`tryCompactMap(_:)`](publisher/trycompactmap(_:).md) to remove `nil` elements from a publisher’s stream based on an error-throwing closure you provide. If the closure throws an error, the publisher cancels the upstream publisher and sends the thrown error to the downstream subscriber as a [`Failure`](publisher/failure.md).

The following example uses an array of numbers as the source for a collection-based publisher. A [`tryCompactMap(_:)`](publisher/trycompactmap(_:).md) operator consumes each integer from the publisher and uses a dictionary to transform the numbers from its Arabic to Roman numerals, as an optional [`String`](https://developer.apple.com/documentation/Swift/String).

If the closure called by [`tryCompactMap(_:)`](publisher/trycompactmap(_:).md) fails to look up a Roman numeral, it returns the optional String `(unknown)`.

If the closure called by [`tryCompactMap(_:)`](publisher/trycompactmap(_:).md) determines the input is `0`, it throws an error. The [`tryCompactMap(_:)`](publisher/trycompactmap(_:).md) operator catches this error and stops publishing, sending a [`Subscribers.Completion.failure(_:)`](subscribers/completion/failure(_:).md) that wraps the error.

```swift
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

- [func filter((Output) -> Bool) -> Optional<Output>.Publisher](just/filter(_:).md)
- [func tryFilter((Self.Output) throws -> Bool) -> Publishers.TryFilter<Self>](just/tryfilter(_:).md)
  Republishes all elements that match a provided error-throwing closure.
- [func compactMap<T>((Output) -> T?) -> Optional<T>.Publisher](just/compactmap(_:).md)
- [func removeDuplicates() -> Just<Output>](just/removeduplicates.md)
- [func removeDuplicates(by: (Output, Output) -> Bool) -> Just<Output>](just/removeduplicates(by:).md)
- [func tryRemoveDuplicates(by: (Output, Output) throws -> Bool) -> Result<Output, any Error>.Publisher](just/tryremoveduplicates(by:).md)
- [func replaceEmpty(with: Output) -> Just<Output>](just/replaceempty(with:).md)
- [func replaceError(with: Output) -> Just<Output>](just/replaceerror(with:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/trycompactmap(_:))*