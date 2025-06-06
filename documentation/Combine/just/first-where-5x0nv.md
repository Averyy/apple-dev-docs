# first(where:)

**Framework**: Combine  
**Kind**: method

Publishes the first element of a stream to satisfy a predicate closure, then finishes normally.

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
func first(where predicate: @escaping (Self.Output) -> Bool) -> Publishers.FirstWhere<Self>
```

#### Return Value

A publisher that only publishes the first element of a stream that satisfies the predicate.

#### Discussion

Use [`first(where:)`](publisher/first(where:).md) to republish only the first element of a stream that satisfies a closure you specify. The publisher ignores all elements after the first element that satisfies the closure and finishes normally. If this publisher doesn’t receive any elements, it finishes without publishing.

In the example below, the provided closure causes the [`Publishers.FirstWhere`](publishers/firstwhere.md) publisher to republish the first received element that’s greater than `0`, then finishes normally.

```swift
let numbers = (-10...10)
cancellable = numbers.publisher
    .first { $0 > 0 }
    .sink { print("\($0)") }

// Prints: "1"
```

## Parameters

- `predicate`: A closure that takes an element as a parameter and returns a Boolean value that indicates whether to publish the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/first(where:)-5x0nv)*