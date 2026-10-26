---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/finish(throwing:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# finish(throwing:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Indicates that the production terminated.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
consuming func finish(throwing error: Failure? = nil)
```

#### Discussion

After all buffered elements are consumed the subsequent call to [`next(isolation:)`](../next%28isolation%29.md) will return `nil` or throw an error.

Calling this function more than once has no effect. After calling finish, the channel enters a terminal state and doesn’t accept new elements.

## Parameters

- `error`: The error to throw, or `nil`, to finish normally.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/finish(throwing:))*