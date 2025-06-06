# setFailureType(to:)

**Framework**: RealityKit  
**Kind**: method

Changes the failure type declared by the upstream publisher.

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
func setFailureType<E>(to failureType: E.Type) -> Publishers.SetFailureType<Self, E> where E : Error
```

#### Return Value

A publisher that appears to send the specified failure type.

#### Discussion

Use [`setFailureType(to:)`](scene/publisher/setfailuretype(to:).md) when you need set the error type of a publisher that cannot fail.

Conversely, if the upstream can fail, you would use [`mapError(_:)`](scene/publisher/maperror(_:).md) to provide instructions on converting the error types to needed by the downstream publisher’s inputs.

The following example has two publishers with mismatched error types: `pub1`’s error type is [`Never`](https://developer.apple.com/documentation/Swift/Never), and `pub2`’s error type is [`Error`](https://developer.apple.com/documentation/Swift/Error). Because of the mismatch, the [`combineLatest(_:)`](scene/publisher/combinelatest(_:).md) operator requires that `pub1` use [`setFailureType(to:)`](scene/publisher/setfailuretype(to:).md) to make it appear that `pub1` can produce the [`Error`](https://developer.apple.com/documentation/Swift/Error) type, like `pub2` can.

```None
let pub1 = [0, 1, 2, 3, 4, 5].publisher
let pub2 = CurrentValueSubject<Int, Error>(0)
let cancellable = pub1
    .setFailureType(to: Error.self)
    .combineLatest(pub2)
    .sink(
        receiveCompletion: { print ("completed: \($0)") },
        receiveValue: { print ("value: \($0)")}
     )

// Prints: "value: (5, 0)".
```

## Parameters

- `failureType`: The   type presented by this publisher.

## See Also

- [func map<T>((Self.Output) -> T) -> Publishers.Map<Self, T>](scene/publisher/map(_:)-6m6k7.md)
  Transforms all elements from the upstream publisher with a provided closure.
- [func tryMap<T>((Self.Output) throws -> T) -> Publishers.TryMap<Self, T>](scene/publisher/trymap(_:).md)
  Transforms all elements from the upstream publisher with a provided error-throwing closure.
- [func flatMap<T, P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Self>](scene/publisher/flatmap(maxpublishers:_:)-9f9ie.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func mapError<E>((Self.Failure) -> E) -> Publishers.MapError<Self, E>](scene/publisher/maperror(_:).md)
  Converts any failure from the upstream publisher into a new error.
- [func replaceNil<T>(with: T) -> Publishers.Map<Self, T>](scene/publisher/replacenil(with:).md)
  Replaces nil elements in the stream with the provided element.
- [func scan<T>(T, (T, Self.Output) -> T) -> Publishers.Scan<Self, T>](scene/publisher/scan(_:_:).md)
  Transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [func tryScan<T>(T, (T, Self.Output) throws -> T) -> Publishers.TryScan<Self, T>](scene/publisher/tryscan(_:_:).md)
  Transforms elements from the upstream publisher by providing the current element to an error-throwing closure along with the last value returned by the closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/publisher/setfailuretype(to:))*