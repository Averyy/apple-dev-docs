---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncbufferedbyteiterator/init(capacity:readfunction:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# init(capacity:readFunction:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: init  
**Role**: Initializer

Creates an asynchronous buffered byte iterator with a specified capacity and read function.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
init(capacity: Int, readFunction: @escaping @Sendable (UnsafeMutableRawBufferPointer) async throws -> Int)
```

## Parameters

- `capacity`: The maximum number of bytes that a single invocation of `readFunction` may produce. This is the allocated capacity of the backing buffer for iteration; the value must be greater than 0.
- `readFunction`: The function for refilling the buffer.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncbufferedbyteiterator/init(capacity:readfunction:))*