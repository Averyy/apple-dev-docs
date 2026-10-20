# deregisterReportHandlers(withClientQueue:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

> **Deprecated**: Pease use deregisterReportHandlersWithQueue:completion:

## Declaration

```swift
func deregisterReportHandlers(withClientQueue queue: dispatch_queue_t, completion: @escaping @Sendable () -> Void)
```

```swift
func deregisterReportHandlers(withClientQueue queue: dispatch_queue_t) async
```

```objc
- (void) deregisterReportHandlersWithClientQueue:(dispatch_queue_t) queue completion:(dispatch_block_t) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbasedevice/deregisterreporthandlers(withclientqueue:completion:))*