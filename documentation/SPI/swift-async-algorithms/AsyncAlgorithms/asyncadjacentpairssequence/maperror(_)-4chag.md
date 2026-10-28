---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncadjacentpairssequence/maperror(_:)-4chag"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# mapError(_:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Converts any failure into a new error.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func mapError<MappedError>(_ transform: @escaping @Sendable (Self.Failure) -> MappedError) -> some Sendable & AsyncSequence<Self.Element, MappedError> where Self : Sendable, MappedError : Error, Self.Element : Sendable
```

## Return Value

An asynchronous sequence that maps the error thrown into the one produced by the transform closure.

## Discussion

Use the [`mapError(_:)`](./maperror%28_%29-4chag.md) operator when you need to replace one error type with another.

## Parameters

- `transform`: A closure that takes the failure as a parameter and returns a new error.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncadjacentpairssequence/maperror(_:)-4chag)*