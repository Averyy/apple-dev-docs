# defaultMaxConcurrentOperationCount

**Framework**: Foundation  
**Kind**: property

The default maximum number of operations to invoke concurrently in a queue.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class let defaultMaxConcurrentOperationCount: Int
```

#### Discussion

The operation queue determines this number dynamically based on current system conditions.

## See Also

- [var qualityOfService: QualityOfService](operationqueue/qualityofservice.md)
  The default service level to apply to operations that the queue invokes.
- [var maxConcurrentOperationCount: Int](operationqueue/maxconcurrentoperationcount.md)
  The maximum number of queued operations that can run at the same time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/defaultmaxconcurrentoperationcount)*