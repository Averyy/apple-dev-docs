# allocate(capacity:as:)

**Framework**: Swift  
**Kind**: method

Allocate uninitialized memory for the specified number of instances of type `T`.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func allocate<T>(capacity: Int, as type: T.Type) -> UnsafeMutableBufferPointer<T>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/executorjob/localallocator/allocate(capacity:as:))*