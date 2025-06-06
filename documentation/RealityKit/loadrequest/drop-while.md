# drop(while:)

**Framework**: RealityKit  
**Kind**: method

Omits elements from the upstream publisher until a given closure returns false, before republishing all remaining elements.

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
func drop(while predicate: @escaping (Self.Output) -> Bool) -> Publishers.DropWhile<Self>
```

#### Return Value

A publisher that skips over elements until the provided closure returns `false`.

#### Discussion

Use `Publisher/drop(while:)` to omit elements from an upstream publisher until the element received meets a condition you specify.

In the example below, the operator omits all elements in the stream until the first element arrives that’s a positive integer, after which the operator publishes all remaining elements:

```None
let numbers = [-62, -1, 0, 10, 0, 22, 41, -1, 5]
cancellable = numbers.publisher
    .drop { $0 <= 0 }
    .sink { print("\($0)") }

// Prints: "10 0, 22 41 -1 5"
```

## Parameters

- `predicate`: A closure that takes an element as a parameter and returns a Boolean value indicating whether to drop the element from the publisher’s output.

## See Also

- [func drop<P>(untilOutputFrom: P) -> Publishers.DropUntilOutput<Self, P>](loadrequest/drop(untiloutputfrom:).md)
  Ignores elements from the upstream publisher until it receives an element from a second publisher.
- [func dropFirst(Int) -> Publishers.Drop<Self>](loadrequest/dropfirst(_:).md)
  Omits the specified number of elements before republishing subsequent elements.
- [func tryDrop(while: (Self.Output) throws -> Bool) -> Publishers.TryDropWhile<Self>](loadrequest/trydrop(while:).md)
  Omits elements from the upstream publisher until an error-throwing closure returns false, before republishing all remaining elements.
- [func prefix(Int) -> Publishers.Output<Self>](loadrequest/prefix(_:).md)
  Republishes elements up to the specified maximum count.
- [func prefix<P>(untilOutputFrom: P) -> Publishers.PrefixUntilOutput<Self, P>](loadrequest/prefix(untiloutputfrom:).md)
  Republishes elements until another publisher emits an element.
- [func prefix(while: (Self.Output) -> Bool) -> Publishers.PrefixWhile<Self>](loadrequest/prefix(while:).md)
  Republishes elements while a predicate closure indicates publishing should continue.
- [func tryPrefix(while: (Self.Output) throws -> Bool) -> Publishers.TryPrefixWhile<Self>](loadrequest/tryprefix(while:).md)
  Republishes elements while an error-throwing predicate closure indicates publishing should continue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/loadrequest/drop(while:))*