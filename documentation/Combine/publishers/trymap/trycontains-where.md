# tryContains(where:)

**Framework**: Combine  
**Kind**: method

Publishes a Boolean value upon receiving an element that satisfies the throwing predicate closure.

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
func tryContains(where predicate: @escaping (Self.Output) throws -> Bool) -> Publishers.TryContainsWhere<Self>
```

#### Return Value

A publisher that emits the Boolean value `true` when the upstream publisher emits a matching value.

#### Discussion

Use [`tryContains(where:)`](publisher/trycontains(where:).md) to find the first element in an upstream that satisfies the error-throwing closure you provide.

This operator consumes elements produced from the upstream publisher until the upstream publisher either:

- Produces a matching element, after which it emits `true` and the publisher finishes normally.
- Emits `false` if no matching element is found and the publisher finishes normally.

If the predicate throws an error, the publisher fails, passing the error to its downstream.

In the example below, the [`tryContains(where:)`](publisher/trycontains(where:).md) operator tests values to find an element less than `10`; when the closure finds an odd number, like `3`, the publisher terminates with an `IllegalValueError`.

```swift
struct IllegalValueError: Error {}

let numbers = [3, 2, 10, 5, 0, 9]
numbers.publisher
    .tryContains {
        if ($0 % 2 != 0) {
            throw IllegalValueError()
        }
       return $0 < 10
    }
    .sink(
        receiveCompletion: { print ("completion: \($0)") },
        receiveValue: { print ("value: \($0)") }
    )

// Prints: "completion: failure(IllegalValueError())"
```

## Parameters

- `predicate`: A closure that takes an element as its parameter and returns a Boolean value that indicates whether the element satisfies the closure’s comparison logic.

## See Also

- [func contains(Self.Output) -> Publishers.Contains<Self>](publishers/trymap/contains(_:).md)
  Publishes a Boolean value upon receiving an element equal to the argument.
- [func contains(where: (Self.Output) -> Bool) -> Publishers.ContainsWhere<Self>](publishers/trymap/contains(where:).md)
  Publishes a Boolean value upon receiving an element that satisfies the predicate closure.
- [func allSatisfy((Self.Output) -> Bool) -> Publishers.AllSatisfy<Self>](publishers/trymap/allsatisfy(_:).md)
  Publishes a single Boolean value that indicates whether all received elements pass a given predicate.
- [func tryAllSatisfy((Self.Output) throws -> Bool) -> Publishers.TryAllSatisfy<Self>](publishers/trymap/tryallsatisfy(_:).md)
  Publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/trymap/trycontains(where:))*