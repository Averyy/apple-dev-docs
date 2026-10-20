# deregisterReportHandlers(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
func deregisterReportHandlers(with queue: dispatch_queue_t, completion: @escaping @Sendable () -> Void)
```

```swift
func deregisterReportHandlers(with queue: dispatch_queue_t) async
```

```objc
- (void) deregisterReportHandlersWithQueue:(dispatch_queue_t) queue completion:(dispatch_block_t) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbasedevice/deregisterreporthandlers(with:completion:))*