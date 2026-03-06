# diagnosticLogs.ProductData

**Framework**: App Store Connect API  
**Kind**: dictionary

The logs and insights for a diagnostic signature.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object diagnosticLogs.ProductData
```

## Topics

### Objects
- [object diagnosticLogs.ProductData.DiagnosticInsights](diagnosticlogs/productdata-data.dictionary/diagnosticinsights-data.dictionary.md)
  Information about an insight including a descriptive string, category, and URL.
- [object diagnosticLogs.ProductData.DiagnosticLogs](diagnosticlogs/productdata-data.dictionary/diagnosticlogs-data.dictionary.md)
  The call stack representation and metadata of the diagnostic log.
- [type DiagnosticInsightDirection](diagnosticinsightdirection.md)
  A string that describes the diagnostic insight direction.
- [type DiagnosticInsightType](diagnosticinsighttype.md)
  A string that desribes the diagnostic insight type.

## Properties

- `signatureId` (string): The opaque resource ID that uniquely identifies a diagnostic signature.
- `diagnosticInsights` ([diagnosticLogs.ProductData.DiagnosticInsights]): An array of insights for a diagnostic signature.
- `diagnosticLogs` ([diagnosticLogs.ProductData.DiagnosticLogs]): An array of logs associated with a diagnostic signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/diagnosticlogs/productdata-data.dictionary)*