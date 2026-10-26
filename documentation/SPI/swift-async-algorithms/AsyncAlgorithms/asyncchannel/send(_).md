---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchannel/send(_:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# send(_:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Sends an element to an awaiting iteration. This function will resume when the next call to `next()` is made or when a call to `finish()` is made from another task. If the channel is already finished then this returns immediately. If the task is cancelled, this function will resume without sending the element. Other sending operations from other tasks will remain active.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func send(_ element: Element) async
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchannel/send(_:))*