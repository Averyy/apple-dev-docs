# allocate(capacity:as:)

**Framework**: Swift  
**Kind**: method

Allocate uninitialized memory for the specified number of instances of type `T`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func allocate<T>(capacity: Int, as type: T.Type) -> UnsafeMutableBufferPointer<T>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/executorjob/localallocator/allocate(capacity:as:))*