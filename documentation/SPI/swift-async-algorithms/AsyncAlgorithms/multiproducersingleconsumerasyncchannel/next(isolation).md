---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/next(isolation:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# next(isolation:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Returns the next element.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
mutating func next(isolation: isolated (any Actor)? = #isolation) async throws(Failure) -> Element?
```

## Return Value

The next buffered element.

## Discussion

If this method returns `nil` it indicates that no further values can ever be returned. The channel automatically closes when all sources have been deinited.

If there are no elements and the channel has not been finished yet, this method will suspend until an element is send to the channel.

If the task calling this method is cancelled this method will return `nil`.

## Parameters

- `isolation`: The callers isolation.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/next(isolation:))*