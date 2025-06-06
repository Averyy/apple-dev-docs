# dropFirst(_:)

**Framework**: RealityKit  
**Kind**: method

Omits the specified number of elements before republishing subsequent elements.

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
func dropFirst(_ count: Int = 1) -> Publishers.Drop<Self>
```

#### Return Value

A publisher that doesn’t republish the first `count` elements.

#### Discussion

Use [`dropFirst(_:)`](scene/publisher/dropfirst(_:).md) when you want to drop the first `n` elements from the upstream publisher, and republish the remaining elements.

The example below drops the first five elements from the stream:

```None
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cancellable = numbers.publisher
    .dropFirst(5)
    .sink { print("\($0)", terminator: " ") }

// Prints: "6 7 8 9 10 "
```

## Parameters

- `count`: The number of elements to omit. The default is  .

## See Also

- [func drop<P>(untilOutputFrom: P) -> Publishers.DropUntilOutput<Self, P>](scene/publisher/drop(untiloutputfrom:).md)
  Ignores elements from the upstream publisher until it receives an element from a second publisher.
- [func drop(while: (Self.Output) -> Bool) -> Publishers.DropWhile<Self>](scene/publisher/drop(while:).md)
  Omits elements from the upstream publisher until a given closure returns false, before republishing all remaining elements.
- [func tryDrop(while: (Self.Output) throws -> Bool) -> Publishers.TryDropWhile<Self>](scene/publisher/trydrop(while:).md)
  Omits elements from the upstream publisher until an error-throwing closure returns false, before republishing all remaining elements.
- [func append(Self.Output...) -> Publishers.Concatenate<Self, Publishers.Sequence<[Self.Output], Self.Failure>>](scene/publisher/append(_:).md)
  Appends a publisher’s output with the specified elements.
- [func prepend(Self.Output...) -> Publishers.Concatenate<Publishers.Sequence<[Self.Output], Self.Failure>, Self>](scene/publisher/prepend(_:).md)
  Prefixes a publisher’s output with the specified values.
- [func prefix(Int) -> Publishers.Output<Self>](scene/publisher/prefix(_:).md)
  Republishes elements up to the specified maximum count.
- [func prefix<P>(untilOutputFrom: P) -> Publishers.PrefixUntilOutput<Self, P>](scene/publisher/prefix(untiloutputfrom:).md)
  Republishes elements until another publisher emits an element.
- [func prefix(while: (Self.Output) -> Bool) -> Publishers.PrefixWhile<Self>](scene/publisher/prefix(while:).md)
  Republishes elements while a predicate closure indicates publishing should continue.
- [func tryPrefix(while: (Self.Output) throws -> Bool) -> Publishers.TryPrefixWhile<Self>](scene/publisher/tryprefix(while:).md)
  Republishes elements while an error-throwing predicate closure indicates publishing should continue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/publisher/dropfirst(_:))*