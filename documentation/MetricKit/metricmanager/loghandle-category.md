# logHandle(category:)

**Framework**: MetricKit  
**Kind**: method

Returns an `OSLog` handle for creating custom signpost metrics that MetricKit aggregates.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
static func logHandle(category: String) -> OSLog
```

## Mentions

- [Monitoring app performance with MetricKit](monitoring-app-performance-with-metrickit.md)

#### Discussion

The method signature and return type are identical; only the type name changes.

```swift
let log = MetricManager.logHandle(category: "rendering")
```

This method replaces [`makeLogHandle(category:)`](mxmetricmanager/makeloghandle(category:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricmanager/loghandle(category:))*