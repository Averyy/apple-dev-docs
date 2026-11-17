# earlyDataStatus

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Whether the request was sent in TLS early data, and whether the server accepted it.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 13.1+
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
var earlyDataStatus: URLSessionTaskMetrics.EarlyDataStatus { get }
```

```objc
@property (readonly) NSURLSessionTaskMetricsEarlyDataStatus earlyDataStatus;
```

## Discussion

Early data isn’t supported in the classic loading mode, where this value is always `NSURLSessionTaskMetricsEarlyDataStatusNotAttempted`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/earlydatastatus)*