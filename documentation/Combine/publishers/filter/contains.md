# contains(_:)

**Framework**: Combine  
**Kind**: method

Publishes a Boolean value upon receiving an element equal to the argument.

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
func contains(_ output: Self.Output) -> Publishers.Contains<Self>
```

#### Return Value

A publisher that emits the Boolean value `true` when the upstream publisher emits a matching value.

#### Discussion

Use [`contains(_:)`](publisher/contains(_:).md) to find the first element in an upstream that’s equal to the supplied argument. The contains publisher consumes all received elements until the upstream publisher produces a matching element. Upon finding the first match, it emits `true` and finishes normally. If the upstream finishes normally without producing a matching element, this publisher emits `false` and finishes.

In the example below, the [`contains(_:)`](publisher/contains(_:).md) operator emits `true` the first time it receives the value `5` from the `numbers.publisher`, and then finishes normally.

```swift
let numbers = [-1, 5, 10, 5]
numbers.publisher
    .contains(5)
    .sink { print("\($0)") }

// Prints: "true"
```

## Parameters

- `output`: An element to match against.

## See Also

- [func contains(where: (Self.Output) -> Bool) -> Publishers.ContainsWhere<Self>](publishers/filter/contains(where:).md)
  Publishes a Boolean value upon receiving an element that satisfies the predicate closure.
- [func tryContains(where: (Self.Output) throws -> Bool) -> Publishers.TryContainsWhere<Self>](publishers/filter/trycontains(where:).md)
  Publishes a Boolean value upon receiving an element that satisfies the throwing predicate closure.
- [func allSatisfy((Self.Output) -> Bool) -> Publishers.AllSatisfy<Self>](publishers/filter/allsatisfy(_:).md)
  Publishes a single Boolean value that indicates whether all received elements pass a given predicate.
- [func tryAllSatisfy((Self.Output) throws -> Bool) -> Publishers.TryAllSatisfy<Self>](publishers/filter/tryallsatisfy(_:).md)
  Publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/filter/contains(_:))*