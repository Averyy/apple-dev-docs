# tryRemoveDuplicates(by:)

**Framework**: Swift  
**Kind**: method

Publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.

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
func tryRemoveDuplicates(by predicate: @escaping (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryRemoveDuplicates<Self>
```

#### Return Value

A publisher that consumes — rather than publishes — duplicate elements.

#### Discussion

Use [`tryRemoveDuplicates(by:)`](optional/publisher-swift.struct/tryremoveduplicates(by:).md) to remove repeating elements from an upstream publisher based upon the evaluation of elements using an error-throwing closure you provide. If your closure throws an error, the publisher terminates with the error.

In the example below, the closure provided to [`tryRemoveDuplicates(by:)`](optional/publisher-swift.struct/tryremoveduplicates(by:).md) returns `true` when two consecutive elements are equal, thereby filtering out `0`, `1`, `2`, and `3`. However, the closure throws an error when it encounters `4`. The publisher then terminates with this error.

```swift
struct BadValuesError: Error {}
let numbers = [0, 0, 0, 0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
cancellable = numbers.publisher
    .tryRemoveDuplicates { first, second -> Bool in
        if (first == 4 && second == 4) {
            throw BadValuesError()
        }
        return first == second
    }
    .sink(
        receiveCompletion: { print ("\($0)") },
        receiveValue: { print ("\($0)", terminator: " ") }
     )

 // Prints: "0 1 2 3 4 failure(BadValuesError()"
```

## Parameters

- `predicate`: A closure to evaluate whether two elements are equivalent, for purposes of filtering. Return   from this closure to indicate that the second element is a duplicate of the first. If this closure throws an error, the publisher terminates with the thrown error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/publisher-swift.struct/tryremoveduplicates(by:))*