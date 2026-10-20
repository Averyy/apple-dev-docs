# commissioning(_:failedWithError:metrics:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Notification that commissioning has failed.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- macOS 26.2+
- tvOS 26.2+
- visionOS 26.2+
- watchOS 26.2+

## Declaration

```swift
optional func commissioning(_ commissioning: MTRCommissioningOperation, failedWithError error: any Error, metrics: MTRMetrics)
```

```objc
- (void) commissioning:(MTRCommissioningOperation *) commissioning failedWithError:(NSError *) error metrics:(MTRMetrics *) metrics;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcommissioningdelegate/commissioning(_:failedwitherror:metrics:))*