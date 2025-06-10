# allocator

**Framework**: Swift  
**Kind**: property

Obtain a stack-disciplined job-local allocator.

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
var allocator: ExecutorJob.LocalAllocator? { get }
```

#### Discussion

If the job does not support allocation, this property will be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/executorjob/allocator)*