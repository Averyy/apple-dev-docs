# stableMetadata

**Framework**: MetricKit  
**Kind**: property

Context dictionary containing state-specific information

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
let stableMetadata: [String : ReportableMetadataValue]
```

#### Discussion

ReportableMetadataValue is defined in the StateReporting framework.

> **Note**: Only stable metadata from StateReporting are aggregated in MetricKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricmanager/reportedstate/stablemetadata)*