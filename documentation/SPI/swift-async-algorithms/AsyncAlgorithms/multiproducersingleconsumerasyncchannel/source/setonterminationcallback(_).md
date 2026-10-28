---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/setonterminationcallback(_:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# setOnTerminationCallback(_:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Sets a callback to invoke when the channel terminated.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func setOnTerminationCallback(_ callback: (@Sendable () -> Void)?)
```

## Discussion

This is called after the last element has been consumed by the channel. If the channel has already terminated this callback is called immediately.

> ❗ **Important**: Only one termination callback can be set per source. Setting a callback if a previous one has been set will override the previous one.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/multiproducersingleconsumerasyncchannel/source/setonterminationcallback(_:))*