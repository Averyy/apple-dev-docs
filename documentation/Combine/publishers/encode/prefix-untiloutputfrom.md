# prefix(untilOutputFrom:)

**Framework**: Combine  
**Kind**: method

Republishes elements until another publisher emits an element.

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
func prefix<P>(untilOutputFrom publisher: P) -> Publishers.PrefixUntilOutput<Self, P> where P : Publisher
```

#### Return Value

A publisher that republishes elements until the second publisher publishes an element.

#### Discussion

After the second publisher publishes an element, the publisher returned by this method finishes.

## Parameters

- `publisher`: A second publisher.

## See Also

- [func drop<P>(untilOutputFrom: P) -> Publishers.DropUntilOutput<Self, P>](publishers/encode/drop(untiloutputfrom:).md)
  Ignores elements from the upstream publisher until it receives an element from a second publisher.
- [func dropFirst(Int) -> Publishers.Drop<Self>](publishers/encode/dropfirst(_:).md)
  Omits the specified number of elements before republishing subsequent elements.
- [func drop(while: (Self.Output) -> Bool) -> Publishers.DropWhile<Self>](publishers/encode/drop(while:).md)
  Omits elements from the upstream publisher until a given closure returns false, before republishing all remaining elements.
- [func tryDrop(while: (Self.Output) throws -> Bool) -> Publishers.TryDropWhile<Self>](publishers/encode/trydrop(while:).md)
  Omits elements from the upstream publisher until an error-throwing closure returns false, before republishing all remaining elements.
- [func append(Self.Output...) -> Publishers.Concatenate<Self, Publishers.Sequence<[Self.Output], Self.Failure>>](publishers/encode/append(_:).md)
  Appends a publisher’s output with the specified elements.
- [func prepend(Self.Output...) -> Publishers.Concatenate<Publishers.Sequence<[Self.Output], Self.Failure>, Self>](publishers/encode/prepend(_:).md)
  Prefixes a publisher’s output with the specified values.
- [func prefix(Int) -> Publishers.Output<Self>](publishers/encode/prefix(_:).md)
  Republishes elements up to the specified maximum count.
- [func prefix(while: (Self.Output) -> Bool) -> Publishers.PrefixWhile<Self>](publishers/encode/prefix(while:).md)
  Republishes elements while a predicate closure indicates publishing should continue.
- [func tryPrefix(while: (Self.Output) throws -> Bool) -> Publishers.TryPrefixWhile<Self>](publishers/encode/tryprefix(while:).md)
  Republishes elements while an error-throwing predicate closure indicates publishing should continue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/encode/prefix(untiloutputfrom:))*