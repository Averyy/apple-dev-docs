# cumulativeAbnormalExitCount

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The number of times the app exited abnormally from the background.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`abnormalTerminationCount`](../backgroundterminationmetric/abnormalterminationcount.md) instead.

## Declaration

```swift
var cumulativeAbnormalExitCount: Int { get }
```

```objc
@property (readonly) NSUInteger cumulativeAbnormalExitCount;
```

#### Discussion

The most common causes of an abnormal exit are uncaught Objective-C exceptions, calls to an abort function, and other conditions resulting in an abort signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxbackgroundexitdata/cumulativeabnormalexitcount)*