# ReportableMetadataIgnored()

**Framework**: StateReporting  
**Kind**: macro

Excludes a property from the generated `metadataDictionary`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@attached
(peer) macro ReportableMetadataIgnored()
```

## Mentions

- [Getting started with StateReporting](getting-started-with-statereporting.md)

#### Overview

Attach `@ReportableMetadataIgnored` to any stored property inside a type annotated with [`ReportableMetadata()`](reportablemetadata().md) to prevent that property from appearing in the generated `metadataDictionary`. Use this for any property you want to omit — for example, properties that hold sensitive data, cached values that derive from other reported metadata, or fields that are unimportant or too verbose to include in metadata reports.

```swift
@ReportableMetadata
struct PaymentMetadata {
    var lastFourDigits: String
    @ReportableMetadataIgnored var rawCardToken: String
}
```

## See Also

- [macro ReportableMetadata()](reportablemetadata().md)
  Automatically generates `ReportableMetadata` conformance for a type.
- [macro ReportableMetadataKey(String)](reportablemetadatakey(_:).md)
  Specifies a custom key name for a property in the generated `metadataDictionary`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/statereporting/reportablemetadataignored())*