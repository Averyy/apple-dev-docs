# last(where:)

**Framework**: Swift  
**Kind**: method

Publishes the last element of a stream that satisfies a predicate closure, after upstream finishes.

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
func last(where predicate: @escaping (Self.Output) -> Bool) -> Publishers.LastWhere<Self>
```

#### Return Value

A publisher that only publishes the last element satisfying the given predicate.

#### Discussion

Use [`last(where:)`](result/publisher-swift.struct/last(where:).md) when you need to republish only the last element of a stream that satisfies a closure you specify.

In the example below, a range publisher emits the last element that satisfies the closure’s criteria, then finishes normally:

```swift
let numbers = (-10...10)
cancellable = numbers.publisher
    .last { $0 < 6 }
    .sink { print("\($0)") }

// Prints: "5"
```

## Parameters

- `predicate`: A closure that takes an element as its parameter and returns a Boolean value that indicates whether to publish the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/publisher-swift.struct/last(where:))*