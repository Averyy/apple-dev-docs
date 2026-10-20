# downloadLog(of:timeout:queue:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 17.6+
- iPadOS 17.6+
- Mac Catalyst 17.6+
- macOS 14.6+
- tvOS 17.6+
- visionOS 1.0+
- watchOS 10.6+

## Declaration

```swift
func downloadLog(of type: MTRDiagnosticLogType, timeout: TimeInterval, queue: dispatch_queue_t, completion: @escaping @Sendable (URL?, (any Error)?) -> Void)
```

```swift
func downloadLog(of type: MTRDiagnosticLogType, timeout: TimeInterval, queue: dispatch_queue_t) async throws -> URL
```

```objc
- (void) downloadLogOfType:(MTRDiagnosticLogType) type timeout:(NSTimeInterval) timeout queue:(dispatch_queue_t) queue completion:(void (^)(NSURL *url, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevice/downloadlog(of:timeout:queue:completion:))*