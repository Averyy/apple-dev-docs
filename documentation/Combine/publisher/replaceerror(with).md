# replaceError(with:)

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

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

In the example below, a publisher of strings fails with a `MyError` instance, which sends a failure completion downstream. The [`replaceError(with:)`](./replaceerror%28with%29.md) operator handles the failure by publishing the string `(replacement element)` and completing normally.

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

This [`replaceError(with:)`](./replaceerror%28with%29.md) functionality is useful when you want to handle an error by sending a single replacement element and end the stream. Use [`catch(_:)`](./catch%28_%29.md) to recover from an error and provide a replacement publisher to continue providing elements to the downstream subscriber.

## Parameters

- `output`: An element to emit when the upstream publisher fails.

## See Also

### Filtering elements
- [func filter((Self.Output) -> Bool) -> Publishers.Filter<Self>](./filter%28_%29.md)
  Republishes all elements that match a provided closure.
- [func tryFilter((Self.Output) throws -> Bool) -> Publishers.TryFilter<Self>](./tryfilter%28_%29.md)
  Republishes all elements that match a provided error-throwing closure.
- [func compactMap<T>((Self.Output) -> T?) -> Publishers.CompactMap<Self, T>](./compactmap%28_%29.md)
  Calls a closure with each received element and publishes any returned optional that has a value.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publisher/replaceerror(with:))*