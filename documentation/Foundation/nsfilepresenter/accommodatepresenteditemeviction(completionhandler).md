# accommodatePresentedItemEviction(completionHandler:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Given that something in the system is waiting to evict the presented file or directory, do whatever it takes to ensure that the eviction will succeed and that the receiver’s application will behave properly when the eviction has happened, and then invoke the completion handler. This must include calling +[NSFileCoordinator removeFilePresenter:]. You may instead prevent eviction by passing the completion handler a meaningful error.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- visionOS 1.1+

## Declaration

```swift
optional func accommodatePresentedItemEviction(completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
optional func accommodatePresentedItemEviction() async throws
```

```objc
- (void) accommodatePresentedItemEvictionWithCompletionHandler:(void (^)(NSError *errorOrNil)) completionHandler;
```

#### Discussion

If this method is not implemented, eviction will fail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilepresenter/accommodatepresenteditemeviction(completionhandler:))*