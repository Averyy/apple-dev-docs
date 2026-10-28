# tryPrefix(while:)

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

Republishes elements while an error-throwing predicate closure indicates publishing should continue.

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
func tryPrefix(while predicate: @escaping (Self.Output) throws -> Bool) -> Publishers.TryPrefixWhile<Self>
```

## Return Value

A publisher that passes through elements until the predicate throws or indicates publishing should finish.

## Discussion

Use [`tryPrefix(while:)`](./tryprefix%28while%29.md) to emit values from the upstream publisher that meet a condition you specify in an error-throwing closure. The publisher finishes when the closure returns `false`. If the closure throws an error, the publisher fails with that error.

```swift
struct OutOfRangeError: Error {}

let numbers = (0...10).reversed()
cancellable = numbers.publisher
    .tryPrefix {
        guard $0 != 0 else {throw OutOfRangeError()}
        return $0 <= numbers.max()!
    }
    .sink(
        receiveCompletion: { print ("completion: \($0)", terminator: " ") },
        receiveValue: { print ("\($0)", terminator: " ") }
    )

// Prints: "10 9 8 7 6 5 4 3 2 1 completion: failure(OutOfRangeError()) "
```

## Parameters

- `predicate`: A closure that takes an element as its parameter and returns a Boolean value indicating whether publishing should continue.

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
- [func prepend<P>(P) -> Publishers.Concatenate<P, Self>](./prepend%28_%29-5dj9c.md)
  Prefixes the output of this publisher with the elements emitted by the given publisher.
- [func prefix(Int) -> Publishers.Output<Self>](./prefix%28_%29.md)
  Republishes elements up to the specified maximum count.
- [func prefix(while: (Self.Output) -> Bool) -> Publishers.PrefixWhile<Self>](./prefix%28while%29.md)
  Republishes elements while a predicate closure indicates publishing should continue.
- [func prefix<P>(untilOutputFrom: P) -> Publishers.PrefixUntilOutput<Self, P>](./prefix%28untiloutputfrom%29.md)
  Republishes elements until another publisher emits an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publisher/tryprefix(while:))*