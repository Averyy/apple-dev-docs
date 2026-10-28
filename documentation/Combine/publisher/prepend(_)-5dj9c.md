# prepend(_:)

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

Prefixes the output of this publisher with the elements emitted by the given publisher.

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
func prepend<P>(_ publisher: P) -> Publishers.Concatenate<P, Self> where P : Publisher, Self.Failure == P.Failure, Self.Output == P.Output
```

## Return Value

A publisher that prefixes the prefixing publisher’s elements prior to this publisher’s elements.

## Discussion

Use [`prepend(_:)`](./prepend%28_%29-5dj9c.md) to publish values from two publishers when you need to prepend one publisher’s elements to another.

In the example below, a publisher of `prefixValues` publishes its elements before the `dataElements` publishes its elements:

```swift
let prefixValues = [0, 1, 255]
let dataElements = (0...10)
cancellable = dataElements.publisher
    .prepend(prefixValues.publisher)
    .sink { print("\($0)", terminator: " ") }

// Prints: "0 1 255 0 1 2 3 4 5 6 7 8 9 10"
```

## Parameters

- `publisher`: The prefixing publisher.

## See Also

### Applying sequence operations to elements
- [func drop<P>(untilOutputFrom: P) -> Publishers.DropUntilOutput<Self, P>](./drop%28untiloutputfrom%29.md)
  Ignores elements from the upstream publisher until it receives an element from a second publisher.
- [func dropFirst(Int) -> Publishers.Drop<Self>](./dropfirst%28_%29.md)
  Omits the specified number of elements before republishing subsequent elements.
- [func drop(while: (Self.Output) -> Bool) -> Publishers.DropWhile<Self>](./drop%28while%29.md)
  Omits elements from the upstream publisher until a given closure returns false, before republishing all remaining elements.
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
- [func prefix(Int) -> Publishers.Output<Self>](./prefix%28_%29.md)
  Republishes elements up to the specified maximum count.
- [func prefix(while: (Self.Output) -> Bool) -> Publishers.PrefixWhile<Self>](./prefix%28while%29.md)
  Republishes elements while a predicate closure indicates publishing should continue.
- [func tryPrefix(while: (Self.Output) throws -> Bool) -> Publishers.TryPrefixWhile<Self>](./tryprefix%28while%29.md)
  Republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [func prefix<P>(untilOutputFrom: P) -> Publishers.PrefixUntilOutput<Self, P>](./prefix%28untiloutputfrom%29.md)
  Republishes elements until another publisher emits an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publisher/prepend(_:)-5dj9c)*