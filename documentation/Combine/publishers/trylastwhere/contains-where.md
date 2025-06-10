# contains(where:)

**Framework**: Combine  
**Kind**: method

Publishes a Boolean value upon receiving an element that satisfies the predicate closure.

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
func contains(where predicate: @escaping (Self.Output) -> Bool) -> Publishers.ContainsWhere<Self>
```

#### Return Value

A publisher that emits the Boolean value `true` when the upstream  publisher emits a matching value.

#### Discussion

Use [`contains(where:)`](publisher/contains(where:).md) to find the first element in an upstream that satisfies the closure you provide. This operator consumes elements produced from the upstream publisher until the upstream publisher produces a matching element.

This operator is useful when the upstream publisher produces elements that don’t conform to `Equatable`.

In the example below, the [`contains(where:)`](publisher/contains(where:).md) operator tests elements against the supplied closure and emits `true` for the first elements that’s greater than `4`, and then finishes normally.

```swift
let numbers = [-1, 0, 10, 5]
numbers.publisher
    .contains {$0 > 4}
    .sink { print("\($0)") }

// Prints: "true"
```

## Parameters

- `predicate`: A closure that takes an element as its parameter and returns a Boolean value that indicates whether the element satisfies the closure’s comparison logic.

## See Also

- [func contains(Self.Output) -> Publishers.Contains<Self>](publishers/trylastwhere/contains(_:).md)
  Publishes a Boolean value upon receiving an element equal to the argument.
- [func tryContains(where: (Self.Output) throws -> Bool) -> Publishers.TryContainsWhere<Self>](publishers/trylastwhere/trycontains(where:).md)
  Publishes a Boolean value upon receiving an element that satisfies the throwing predicate closure.
- [func allSatisfy((Self.Output) -> Bool) -> Publishers.AllSatisfy<Self>](publishers/trylastwhere/allsatisfy(_:).md)
  Publishes a single Boolean value that indicates whether all received elements pass a given predicate.
- [func tryAllSatisfy((Self.Output) throws -> Bool) -> Publishers.TryAllSatisfy<Self>](publishers/trylastwhere/tryallsatisfy(_:).md)
  Publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/trylastwhere/contains(where:))*