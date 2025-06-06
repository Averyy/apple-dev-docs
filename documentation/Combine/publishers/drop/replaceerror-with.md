# replaceError(with:)

**Framework**: Combine  
**Kind**: method

Replaces any errors in the stream with the provided element.

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
func replaceError(with output: Self.Output) -> Publishers.ReplaceError<Self>
```

#### Return Value

A publisher that replaces an error from the upstream publisher with the provided output element.

#### Discussion

If the upstream publisher fails with an error, this publisher emits the provided element, then finishes normally.

In the example below, a publisher of strings fails with a `MyError` instance, which sends a failure completion downstream. The [`replaceError(with:)`](publisher/replaceerror(with:).md) operator handles the failure by publishing the string `(replacement element)` and completing normally.

```swift
struct MyError: Error {}
let fail = Fail<String, MyError>(error: MyError())
cancellable = fail
    .replaceError(with: "(replacement element)")
    .sink(
        receiveCompletion: { print ("\($0)") },
        receiveValue: { print ("\($0)", terminator: " ") }
    )

// Prints: "(replacement element) finished".
```

This [`replaceError(with:)`](publisher/replaceerror(with:).md) functionality is useful when you want to handle an error by sending a single replacement element and end the stream. Use [`catch(_:)`](publisher/catch(_:).md) to recover from an error and provide a replacement publisher to continue providing elements to the downstream subscriber.

## Parameters

- `output`: An element to emit when the upstream publisher fails.

## See Also

- [func filter((Self.Output) -> Bool) -> Publishers.Filter<Self>](publishers/drop/filter(_:).md)
  Republishes all elements that match a provided closure.
- [func tryFilter((Self.Output) throws -> Bool) -> Publishers.TryFilter<Self>](publishers/drop/tryfilter(_:).md)
  Republishes all elements that match a provided error-throwing closure.
- [func compactMap<T>((Self.Output) -> T?) -> Publishers.CompactMap<Self, T>](publishers/drop/compactmap(_:).md)
  Calls a closure with each received element and publishes any returned optional that has a value.
- [func tryCompactMap<T>((Self.Output) throws -> T?) -> Publishers.TryCompactMap<Self, T>](publishers/drop/trycompactmap(_:).md)
  Calls an error-throwing closure with each received element and publishes any returned optional that has a value.
- [func removeDuplicates() -> Publishers.RemoveDuplicates<Self>](publishers/drop/removeduplicates.md)
  Publishes only elements that don’t match the previous element.
- [func removeDuplicates(by: (Self.Output, Self.Output) -> Bool) -> Publishers.RemoveDuplicates<Self>](publishers/drop/removeduplicates(by:).md)
  Publishes only elements that don’t match the previous element, as evaluated by a provided closure.
- [func tryRemoveDuplicates(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryRemoveDuplicates<Self>](publishers/drop/tryremoveduplicates(by:).md)
  Publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [func replaceEmpty(with: Self.Output) -> Publishers.ReplaceEmpty<Self>](publishers/drop/replaceempty(with:).md)
  Replaces an empty stream with the provided element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/drop/replaceerror(with:))*