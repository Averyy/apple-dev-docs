# allocator

**Framework**: Swift  
**Kind**: property

Obtain a stack-disciplined job-local allocator.

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
var allocator: ExecutorJob.LocalAllocator? { get }
```

#### Discussion

If the job does not support allocation, this property will be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/executorjob/allocator)*