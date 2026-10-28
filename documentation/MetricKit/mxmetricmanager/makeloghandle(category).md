# makeLogHandle(category:)

**Framework**: MetricKit  
**Kind**: method  
**Role**: Type Method

Returns a log handle used for writing custom metric events.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`logHandle(category:)`](../metricmanager/loghandle%28category%29.md) instead.

## Declaration

```swift
class func makeLogHandle(category: String) -> OSLog
```

```objc
+ (os_log_t) makeLogHandleWithCategory:(NSString *) category;
```

## Return Value

A customized [`OSLog`](../../os/oslog.md) object used for writing custom metrics of the same category.

## Discussion

The object returned by this method saves only custom signpost metrics. Other kinds of [`os_log`](../../os/os_log.md) messages aren’t persisted.

## Parameters

- `category`: A developer-specified string containing the name of the category of custom metrics written to the log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricmanager/makeloghandle(category:))*