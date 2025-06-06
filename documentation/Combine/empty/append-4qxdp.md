# append(_:)

**Framework**: Combine  
**Kind**: method

Appends the output of this publisher with the elements emitted by the given publisher.

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
func append<P>(_ publisher: P) -> Publishers.Concatenate<Self, P> where P : Publisher, Self.Failure == P.Failure, Self.Output == P.Output
```

#### Return Value

A publisher that appends the appending publisher’s elements after this publisher’s elements.

#### Discussion

Use [`append(_:)`](publisher/append(_:)-5yh02.md) to append the output of one publisher to another. The [`append(_:)`](publisher/append(_:)-5yh02.md) operator produces no elements until this publisher finishes. It then produces this publisher’s elements, followed by the given publisher’s elements. If this publisher fails with an error, the given publishers elements aren’t published.

In the example below, the `append` publisher republishes all elements from the `numbers` publisher until it finishes, then publishes all elements from the `otherNumbers` publisher:

```swift
let numbers = (0...10)
let otherNumbers = (25...35)
cancellable = numbers.publisher
    .append(otherNumbers.publisher)
    .sink { print("\($0)", terminator: " ") }

// Prints: "0 1 2 3 4 5 6 7 8 9 10 25 26 27 28 29 30 31 32 33 34 35 "
```

## Parameters

- `publisher`: The appending publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/empty/append(_:)-4qxdp)*