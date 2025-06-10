# cumulativeAbnormalExitCount

**Framework**: MetricKit  
**Kind**: property

The number of times the app exited abnormally from the background.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var cumulativeAbnormalExitCount: Int { get }
```

#### Discussion

The most common causes of an abnormal exit are uncaught Objective-C exceptions, calls to an abort function, and other conditions resulting in an abort signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxbackgroundexitdata/cumulativeabnormalexitcount)*