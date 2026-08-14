# StateReporting

**Framework**: StateReporting  
**Kind**: module

Communicate your app’s state to the system to improve diagnostic actionability.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

#### Overview

StateReporting lets you define named domains and emit structured state transitions from your app. [`MetricKit`](https://developer.apple.com/documentation/metrickit) surfaces state context in both state-aggregated and interval-level metric entries. Instruments displays transitions in the Points of Interest instrument so you can cross-reference app state against other profiling data.

Each domain holds up to one active state at a time, and you can combine states across domains. For example, your game can track its graphics configuration in one domain and its game mode in another, so you can compare performance across every state combination.

## Topics

### Essentials
- [Getting started with StateReporting](getting-started-with-statereporting.md)
  Define reportable metadata types, obtain a state reporter for your domain, and report transitions at the right call sites in your app.
### Reporting
- [class StateReporter](statereporter.md)
  An object unique per domain that records state transitions and volatile metadata updates.
### Defining metadata
- [protocol ReportableMetadata](reportablemetadata.md)
  A protocol for types that can supply their metadata as a dictionary of reportable values.
- [enum ReportableMetadataValue](reportablemetadatavalue.md)
  A value in a reportable-metadata dictionary.
### Metadata type macros
- [macro ReportableMetadata()](reportablemetadata().md)
  Automatically generates `ReportableMetadata` conformance for a type.
- [macro ReportableMetadataKey(String)](reportablemetadatakey(_:).md)
  Specifies a custom key name for a property in the generated `metadataDictionary`.
- [macro ReportableMetadataIgnored()](reportablemetadataignored().md)
  Excludes a property from the generated `metadataDictionary`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/StateReporting)*