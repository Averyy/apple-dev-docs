# tryFirst(where:)

**Framework**: Swift  
**Kind**: method

Publishes the first element of a stream to satisfy a throwing predicate closure, then finishes normally.

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
func tryFirst(where predicate: @escaping (Self.Output) throws -> Bool) -> Publishers.TryFirstWhere<Self>
```

#### Return Value

A publisher that only publishes the first element of a stream that satisfies the predicate.

#### Discussion

Use [`tryFirst(where:)`](optional/publisher-swift.struct/tryfirst(where:).md) when you need to republish only the first element of a stream that satisfies an error-throwing closure you specify. The publisher ignores all elements after the first. If this publisher doesn’t receive any elements, it finishes without publishing. If the predicate closure throws an error, the publisher fails.

In the example below, a range publisher emits the first element in the range then finishes normally:

```swift
let numberRange: ClosedRange<Int> = (-1...50)
numberRange.publisher
    .tryFirst {
        guard $0 < 99 else {throw RangeError()}
        return true
    }
    .sink(
        receiveCompletion: { print ("completion: \($0)", terminator: " ") },
        receiveValue: { print ("\($0)", terminator: " ") }
     )

// Prints: "-1 completion: finished"
// If instead the number range were ClosedRange<Int> = (100...200), the tryFirst operator would terminate publishing with a RangeError.
```

## Parameters

- `predicate`: A closure that takes an element as a parameter and returns a Boolean value that indicates whether to publish the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/publisher-swift.struct/tryfirst(where:))*