# makeLogHandle(category:)

**Framework**: MetricKit  
**Kind**: method

Returns a log handle used for writing custom metric events.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class func makeLogHandle(category: String) -> OSLog
```

#### Return Value

A customized [`OSLog`](https://developer.apple.com/documentation/os/OSLog) object used for writing custom metrics of the same category.

#### Discussion

The object returned by this method saves only custom signpost metrics. Other kinds of [`os_log`](https://developer.apple.com/documentation/os/os_log) messages aren’t persisted.

## Parameters

- `category`: A developer-specified string containing the name of the category of custom metrics written to the log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricmanager/makeloghandle(category:))*