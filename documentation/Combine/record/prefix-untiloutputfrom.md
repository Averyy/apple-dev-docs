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

- [func drop<P>(untilOutputFrom: P) -> Publishers.DropUntilOutput<Self, P>](record/drop(untiloutputfrom:).md)
  Ignores elements from the upstream publisher until it receives an element from a second publisher.
- [func dropFirst(Int) -> Publishers.Drop<Self>](record/dropfirst(_:).md)
  Omits the specified number of elements before republishing subsequent elements.
- [func drop(while: (Self.Output) -> Bool) -> Publishers.DropWhile<Self>](record/drop(while:).md)
  Omits elements from the upstream publisher until a given closure returns false, before republishing all remaining elements.
- [func tryDrop(while: (Self.Output) throws -> Bool) -> Publishers.TryDropWhile<Self>](record/trydrop(while:).md)
  Omits elements from the upstream publisher until an error-throwing closure returns false, before republishing all remaining elements.
- [func prefix(Int) -> Publishers.Output<Self>](record/prefix(_:).md)
  Republishes elements up to the specified maximum count.
- [func prefix(while: (Self.Output) -> Bool) -> Publishers.PrefixWhile<Self>](record/prefix(while:).md)
  Republishes elements while a predicate closure indicates publishing should continue.
- [func tryPrefix(while: (Self.Output) throws -> Bool) -> Publishers.TryPrefixWhile<Self>](record/tryprefix(while:).md)
  Republishes elements while an error-throwing predicate closure indicates publishing should continue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/record/prefix(untiloutputfrom:))*