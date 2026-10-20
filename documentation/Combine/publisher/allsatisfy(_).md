# allSatisfy(_:)

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

Publishes a single Boolean value that indicates whether all received elements pass a given predicate.

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
func allSatisfy(_ predicate: @escaping (Self.Output) -> Bool) -> Publishers.AllSatisfy<Self>
```

#### Return Value

A publisher that publishes a Boolean value that indicates whether all received elements pass a given predicate.

#### Discussion

Use the [`allSatisfy(_:)`](./allsatisfy%28_%29.md) operator to determine if all elements in a stream satisfy a criteria you provide. When this publisher receives an element, it runs the predicate against the element. If the predicate returns `false`, the publisher produces a `false` value and finishes. If the upstream publisher finishes normally, this publisher produces a `true` value and finishes.

In the example below, the [`allSatisfy(_:)`](./allsatisfy%28_%29.md) operator tests if each an integer array publisher’s elements fall into the `targetRange`:

```swift
let targetRange = (-1...100)
let numbers = [-1, 0, 10, 5]
numbers.publisher
    .allSatisfy { targetRange.contains($0) }
    .sink { print("\($0)") }

// Prints: "true"
```

With operators similar to [`reduce(_:_:)`](./reduce%28_,_%29.md), this publisher produces at most one value.

> **Note**: Upon receiving any request greater than zero, this publisher requests unlimited elements from the upstream publisher.

## Parameters

- `predicate`: A closure that evaluates each received element. Return `true` to continue, or `false` to cancel the upstream and complete.

## See Also

### Applying matching criteria to elements
- [func contains(Self.Output) -> Publishers.Contains<Self>](./contains%28_%29.md)
  Publishes a Boolean value upon receiving an element equal to the argument.
- [func contains(where: (Self.Output) -> Bool) -> Publishers.ContainsWhere<Self>](./contains%28where%29.md)
  Publishes a Boolean value upon receiving an element that satisfies the predicate closure.
- [func tryContains(where: (Self.Output) throws -> Bool) -> Publishers.TryContainsWhere<Self>](./trycontains%28where%29.md)
  Publishes a Boolean value upon receiving an element that satisfies the throwing predicate closure.
- [func tryAllSatisfy((Self.Output) throws -> Bool) -> Publishers.TryAllSatisfy<Self>](./tryallsatisfy%28_%29.md)
  Publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publisher/allsatisfy(_:))*