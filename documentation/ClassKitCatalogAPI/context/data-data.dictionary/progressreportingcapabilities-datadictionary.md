# Context.Data.ProgressReportingCapabilities

**Framework**: ClassKit Catalog API  
**Kind**: dictionary

The progress reporting capabilities supported by a context.

**Availability**:
- ClassKit 1.0+

## Declaration

```swift
object Context.Data.ProgressReportingCapabilities
```

#### Discussion

When creating a context, if you don’t specify a progress reporting capability with `kind` set to `duration`, the system adds one automatically, using an empty string for the `details` field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkitcatalogapi/context/data-data.dictionary/progressreportingcapabilities-data.dictionary)*