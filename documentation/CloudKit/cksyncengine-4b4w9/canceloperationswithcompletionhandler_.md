# cancelOperationsWithCompletionHandler:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Cancels any in-progress or pending sync operations.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
- (void) cancelOperationsWithCompletionHandler:(void (^)()) completionHandler;
```

## Discussion

The sync engine processes cancellation requests asynchronously, meaning it’s possible for in-progress operations to complete even after this method returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-4b4w9/canceloperationswithcompletionhandler:)*