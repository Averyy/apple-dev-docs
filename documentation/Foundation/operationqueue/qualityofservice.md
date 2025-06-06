# qualityOfService

**Framework**: Foundation  
**Kind**: property

The default service level to apply to operations that the queue invokes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var qualityOfService: QualityOfService { get set }
```

#### Discussion

This property specifies the service level applied to operation objects added to the queue. If the operation object has an explicit service level set, that value is used instead. The default value of this property depends on how you created the queue. For queues you create yourself, the default value is `NSOperationQualityOfServiceBackground`. For the queue returned by the [`main`](operationqueue/main.md) method, the default value is `NSOperationQualityOfServiceUserInteractive` and cannot be changed.

Service levels affect the priority with which operation objects are given access to system resources such as CPU time, network resources, disk resources, and so on. Operations with a higher quality of service level are given greater priority over system resources so that they may perform their task more quickly. You use service levels to ensure that operations responding to explicit user requests are given priority over less critical work.

## See Also

- [var maxConcurrentOperationCount: Int](operationqueue/maxconcurrentoperationcount.md)
  The maximum number of queued operations that can run at the same time.
- [class let defaultMaxConcurrentOperationCount: Int](operationqueue/defaultmaxconcurrentoperationcount.md)
  The default maximum number of operations to invoke concurrently in a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operationqueue/qualityofservice)*