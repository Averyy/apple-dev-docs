---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncthrowingchannel/fail(_:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# fail(_:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Sends an error to all awaiting iterations. All subsequent calls to `next(_:)` will resume immediately.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func fail(_ error: any Error) where Failure == any Error
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncthrowingchannel/fail(_:))*