# loadVideoPerformanceMetrics(completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func loadVideoPerformanceMetrics(completionHandler: @escaping @Sendable (AVVideoPerformanceMetrics?) -> Void)
```

```swift
var videoPerformanceMetrics: AVVideoPerformanceMetrics? { get async }
```

```objc
- (void) loadVideoPerformanceMetricsWithCompletionHandler:(void (^)(AVVideoPerformanceMetrics *videoPerformanceMetrics)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/loadvideoperformancemetrics(completionhandler:))*