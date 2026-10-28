# drop(while:)

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

Omits elements from the upstream publisher until a given closure returns false, before republishing all remaining elements.

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
func drop(while predicate: @escaping (Self.Output) -> Bool) -> Publishers.DropWhile<Self>
```

## Return Value

A publisher that skips over elements until the provided closure returns `false`.

## Discussion

Use [`drop(while:)`](./drop%28while%29.md) to omit elements from an upstream publisher until the element received meets a condition you specify.

In the example below, the operator omits all elements in the stream until the first element arrives that’s a positive integer, after which the operator publishes all remaining elements:

```swift
let numbers = [-62, -1, 0, 10, 0, 22, 41, -1, 5]
cancellable = numbers.publisher
    .drop { $0 <= 0 }
    .sink { print("\($0)") }

// Prints: "10 0, 22 41 -1 5"
```

## Parameters

- `predicate`: A closure that takes an element as a parameter and returns a Boolean value indicating whether to drop the element from the publisher’s output.

## See Also

### Applying sequence operations to elements
- [func drop<P>(untilOutputFrom: P) -> Publishers.DropUntilOutput<Self, P>](./drop%28untiloutputfrom%29.md)
  Ignores elements from the upstream publisher until it receives an element from a second publisher.
- [func dropFirst(Int) -> Publishers.Drop<Self>](./dropfirst%28_%29.md)
  Omits the specified number of elements before republishing subsequent elements.
- [func tryDrop(while: (Self.Output) throws -> Bool) -> Publishers.TryDropWhile<Self>](./trydrop%28while%29.md)
  Omits elements from the upstream publisher until an error-throwing closure returns false, before republishing all remaining elements.
- [func append(Self.Output...) -> Publishers.Concatenate<Self, Publishers.Sequence<[Self.Output], Self.Failure>>](./append%28_%29-1qb8d.md)
  Appends a publisher’s output with the specified elements.
- [func append<S>(S) -> Publishers.Concatenate<Self, Publishers.Sequence<S, Self.Failure>>](./append%28_%29-69sdn.md)
  Appends a publisher’s output with the specified sequence.
- [func append<P>(P) -> Publishers.Concatenate<Self, P>](./append%28_%29-5yh02.md)
  Appends the output of this publisher with the elements emitted by the given publisher.
- [func prepend(Self.Output...) -> Publishers.Concatenate<Publishers.Sequence<[Self.Output], Self.Failure>, Self>](./prepend%28_%29-7wk5l.md)
  Prefixes a publisher’s output with the specified values.
- [func prepend<S>(S) -> Publishers.Concatenate<Publishers.Sequence<S, Self.Failure>, Self>](./prepend%28_%29-v9sb.md)
  Prefixes a publisher’s output with the specified sequence.
- [func prepend<P>(P) -> Publishers.Concatenate<P, Self>](./prepend%28_%29-5dj9c.md)
  Prefixes the output of this publisher with the elements emitted by the given publisher.
- [func prefix(Int) -> Publishers.Output<Self>](./prefix%28_%29.md)
  Republishes elements up to the specified maximum count.
- [func prefix(while: (Self.Output) -> Bool) -> Publishers.PrefixWhile<Self>](./prefix%28while%29.md)
  Republishes elements while a predicate closure indicates publishing should continue.
- [func tryPrefix(while: (Self.Output) throws -> Bool) -> Publishers.TryPrefixWhile<Self>](./tryprefix%28while%29.md)
  Republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [func prefix<P>(untilOutputFrom: P) -> Publishers.PrefixUntilOutput<Self, P>](./prefix%28untiloutputfrom%29.md)
  Republishes elements until another publisher emits an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publisher/drop(while:))*