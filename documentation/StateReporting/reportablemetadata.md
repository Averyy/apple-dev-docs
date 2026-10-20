# ReportableMetadata

**Framework**: StateReporting  
**Kind**: protocol  
**Role**: Protocol

A protocol for types that can supply their metadata as a dictionary of reportable values.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
protocol ReportableMetadata
```

## Mentions

- [Getting started with StateReporting](./getting-started-with-statereporting.md)

#### Overview

Adopt `ReportableMetadata` to pass stable or volatile metadata to [`StateReporter`](./statereporter.md). The single required property, [`metadataDictionary`](./reportablemetadata/metadatadictionary.md), maps string keys to [`ReportableMetadataValue`](./reportablemetadatavalue.md) cases. Use the [`ReportableMetadata()`](./reportablemetadata%28%29.md) macro to synthesize the conformance automatically from stored properties, rather than implementing it by hand.

## Topics

### Instance Properties
- [var metadataDictionary: [String : ReportableMetadataValue]](./reportablemetadata/metadatadictionary.md)
  A dictionary mapping string keys to reportable values that describes the current metadata.

## See Also

### Defining metadata
- [enum ReportableMetadataValue](./reportablemetadatavalue.md)
  A value in a reportable-metadata dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/statereporting/reportablemetadata)*