# compactMap(_:)

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

Calls a closure with each received element and publishes any returned optional that has a value.

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
func compactMap<T>(_ transform: @escaping (Self.Output) -> T?) -> Publishers.CompactMap<Self, T>
```

## Return Value

Any non-`nil` optional results of the calling the supplied closure.

## Discussion

Combine’s [`compactMap(_:)`](./compactmap%28_%29.md) operator performs a function similar to that of [`compactMap(_:)`](../../Swift/sequence/compactmap%28_%29.md) in the Swift standard library: the [`compactMap(_:)`](./compactmap%28_%29.md) operator in Combine removes `nil` elements in a publisher’s stream and republishes non-`nil` elements to the downstream subscriber.

The example below uses a range of numbers as the source for a collection based publisher. The [`compactMap(_:)`](./compactmap%28_%29.md) operator consumes each element from the `numbers` publisher attempting to access the dictionary using the element as the key. If the example’s dictionary returns a `nil`, due to a non-existent key, [`compactMap(_:)`](./compactmap%28_%29.md) filters out the `nil` (missing) elements.

```swift
let numbers = (0...5)
let romanNumeralDict: [Int : String] =
    [1: "I", 2: "II", 3: "III", 5: "V"]

cancellable = numbers.publisher
    .compactMap { romanNumeralDict[$0] }
    .sink { print("\($0)", terminator: " ") }

// Prints: "I II III V"
```

## Parameters

- `transform`: A closure that receives a value and returns an optional value.

## See Also

### Filtering elements
- [func filter((Self.Output) -> Bool) -> Publishers.Filter<Self>](./filter%28_%29.md)
  Republishes all elements that match a provided closure.
- [func tryFilter((Self.Output) throws -> Bool) -> Publishers.TryFilter<Self>](./tryfilter%28_%29.md)
  Republishes all elements that match a provided error-throwing closure.
- [func tryCompactMap<T>((Self.Output) throws -> T?) -> Publishers.TryCompactMap<Self, T>](./trycompactmap%28_%29.md)
  Calls an error-throwing closure with each received element and publishes any returned optional that has a value.
- [func removeDuplicates() -> Publishers.RemoveDuplicates<Self>](./removeduplicates%28%29.md)
  Publishes only elements that don’t match the previous element.
- [func removeDuplicates(by: (Self.Output, Self.Output) -> Bool) -> Publishers.RemoveDuplicates<Self>](./removeduplicates%28by%29.md)
  Publishes only elements that don’t match the previous element, as evaluated by a provided closure.
- [func tryRemoveDuplicates(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryRemoveDuplicates<Self>](./tryremoveduplicates%28by%29.md)
  Publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [func replaceEmpty(with: Self.Output) -> Publishers.ReplaceEmpty<Self>](./replaceempty%28with%29.md)
  Replaces an empty stream with the provided element.
- [func replaceError(with: Self.Output) -> Publishers.ReplaceError<Self>](./replaceerror%28with%29.md)
  Replaces any errors in the stream with the provided element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publisher/compactmap(_:))*