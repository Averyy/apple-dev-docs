# prefix(while:)

**Framework**: Combine  
**Kind**: method

Republishes elements while a predicate closure indicates publishing should continue.

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
func prefix(while predicate: @escaping (Self.Output) -> Bool) -> Publishers.PrefixWhile<Self>
```

#### Return Value

A publisher that passes through elements until the predicate indicates publishing should finish.

#### Discussion

Use [`prefix(while:)`](publisher/prefix(while:).md) to emit values while elements from the upstream publisher meet a condition you specify. The publisher finishes when the closure returns `false`.

In the example below, the [`prefix(while:)`](publisher/prefix(while:).md) operator emits values while the element it receives is less than five:

```swift
let numbers = (0...10)
numbers.publisher
    .prefix { $0 < 5 }
    .sink { print("\($0)", terminator: " ") }

// Prints: "0 1 2 3 4"
```

## Parameters

- `predicate`: A closure that takes an element as its parameter and returns a Boolean value that indicates whether publishing should continue.

## See Also

- [func drop<P>(untilOutputFrom: P) -> Publishers.DropUntilOutput<Self, P>](publishers/tryfilter/drop(untiloutputfrom:).md)
  Ignores elements from the upstream publisher until it receives an element from a second publisher.
- [func dropFirst(Int) -> Publishers.Drop<Self>](publishers/tryfilter/dropfirst(_:).md)
  Omits the specified number of elements before republishing subsequent elements.
- [func drop(while: (Self.Output) -> Bool) -> Publishers.DropWhile<Self>](publishers/tryfilter/drop(while:).md)
  Omits elements from the upstream publisher until a given closure returns false, before republishing all remaining elements.
- [func tryDrop(while: (Self.Output) throws -> Bool) -> Publishers.TryDropWhile<Self>](publishers/tryfilter/trydrop(while:).md)
  Omits elements from the upstream publisher until an error-throwing closure returns false, before republishing all remaining elements.
- [func append(Self.Output...) -> Publishers.Concatenate<Self, Publishers.Sequence<[Self.Output], Self.Failure>>](publishers/tryfilter/append(_:).md)
  Appends a publisher’s output with the specified elements.
- [func prepend(Self.Output...) -> Publishers.Concatenate<Publishers.Sequence<[Self.Output], Self.Failure>, Self>](publishers/tryfilter/prepend(_:).md)
  Prefixes a publisher’s output with the specified values.
- [func prefix(Int) -> Publishers.Output<Self>](publishers/tryfilter/prefix(_:).md)
  Republishes elements up to the specified maximum count.
- [func tryPrefix(while: (Self.Output) throws -> Bool) -> Publishers.TryPrefixWhile<Self>](publishers/tryfilter/tryprefix(while:).md)
  Republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [func prefix<P>(untilOutputFrom: P) -> Publishers.PrefixUntilOutput<Self, P>](publishers/tryfilter/prefix(untiloutputfrom:).md)
  Republishes elements until another publisher emits an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/tryfilter/prefix(while:))*