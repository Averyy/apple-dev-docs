# prefix(_:)

**Framework**: Combine  
**Kind**: method

Republishes elements up to the specified maximum count.

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
func prefix(_ maxLength: Int) -> Publishers.Output<Self>
```

#### Return Value

A publisher that publishes up to the specified number of elements.

#### Discussion

Use [`prefix(_:)`](publisher/prefix(_:).md) to limit the number of elements republished to the downstream subscriber.

In the example below, the [`prefix(_:)`](publisher/prefix(_:).md) operator limits its output to the first two elements before finishing normally:

```swift
let numbers = (0...10)
cancellable = numbers.publisher
    .prefix(2)
    .sink { print("\($0)", terminator: " ") }

// Prints: "0 1"
```

## Parameters

- `maxLength`: The maximum number of elements to republish.

## See Also

- [func drop<P>(untilOutputFrom: P) -> Publishers.DropUntilOutput<Self, P>](publisher/drop(untiloutputfrom:).md)
  Ignores elements from the upstream publisher until it receives an element from a second publisher.
- [func dropFirst(Int) -> Publishers.Drop<Self>](publisher/dropfirst(_:).md)
  Omits the specified number of elements before republishing subsequent elements.
- [func drop(while: (Self.Output) -> Bool) -> Publishers.DropWhile<Self>](publisher/drop(while:).md)
  Omits elements from the upstream publisher until a given closure returns false, before republishing all remaining elements.
- [func tryDrop(while: (Self.Output) throws -> Bool) -> Publishers.TryDropWhile<Self>](publisher/trydrop(while:).md)
  Omits elements from the upstream publisher until an error-throwing closure returns false, before republishing all remaining elements.
- [func append(Self.Output...) -> Publishers.Concatenate<Self, Publishers.Sequence<[Self.Output], Self.Failure>>](publisher/append(_:)-1qb8d.md)
  Appends a publisher’s output with the specified elements.
- [func append<S>(S) -> Publishers.Concatenate<Self, Publishers.Sequence<S, Self.Failure>>](publisher/append(_:)-69sdn.md)
  Appends a publisher’s output with the specified sequence.
- [func append<P>(P) -> Publishers.Concatenate<Self, P>](publisher/append(_:)-5yh02.md)
  Appends the output of this publisher with the elements emitted by the given publisher.
- [func prepend(Self.Output...) -> Publishers.Concatenate<Publishers.Sequence<[Self.Output], Self.Failure>, Self>](publisher/prepend(_:)-7wk5l.md)
  Prefixes a publisher’s output with the specified values.
- [func prepend<S>(S) -> Publishers.Concatenate<Publishers.Sequence<S, Self.Failure>, Self>](publisher/prepend(_:)-v9sb.md)
  Prefixes a publisher’s output with the specified sequence.
- [func prepend<P>(P) -> Publishers.Concatenate<P, Self>](publisher/prepend(_:)-5dj9c.md)
  Prefixes the output of this publisher with the elements emitted by the given publisher.
- [func prefix(while: (Self.Output) -> Bool) -> Publishers.PrefixWhile<Self>](publisher/prefix(while:).md)
  Republishes elements while a predicate closure indicates publishing should continue.
- [func tryPrefix(while: (Self.Output) throws -> Bool) -> Publishers.TryPrefixWhile<Self>](publisher/tryprefix(while:).md)
  Republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [func prefix<P>(untilOutputFrom: P) -> Publishers.PrefixUntilOutput<Self, P>](publisher/prefix(untiloutputfrom:).md)
  Republishes elements until another publisher emits an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publisher/prefix(_:))*