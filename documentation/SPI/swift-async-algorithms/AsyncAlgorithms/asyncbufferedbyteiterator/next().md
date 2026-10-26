---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncbufferedbyteiterator/next()"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# next()

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Reads a byte out of the buffer if available. When no bytes are available, this will trigger the read function to reload the buffer and then return the next byte from that buffer.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
mutating func next() async throws -> UInt8?
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncbufferedbyteiterator/next())*