# stableMetadata

**Framework**: MetricKit  
**Kind**: property

Context dictionary containing state-specific information

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
let stableMetadata: [String : ReportableMetadataValue]
```

#### Discussion

ReportableMetadataValue is defined in the StateReporting framework.

> **Note**: Only stable metadata from StateReporting are aggregated in MetricKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metricmanager/reportedstate/stablemetadata)*