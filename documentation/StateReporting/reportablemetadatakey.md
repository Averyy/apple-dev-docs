# ReportableMetadataKey(_:)

**Framework**: StateReporting  
**Kind**: macro

Specifies a custom key name for a property in the generated `metadataDictionary`.

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
(peer) macro ReportableMetadataKey(_ key: String)
```

## Mentions

- [Getting started with StateReporting](getting-started-with-statereporting.md)

#### Overview

By default, property names are used as dictionary keys. Use this macro to provide a different key name, such as for compatibility with server APIs or naming conventions.

```swift
@ReportableMetadata
struct SessionMetadata {
    @ReportableMetadataKey("uid") var userID: String
    var region: String
}
```

## See Also

- [macro ReportableMetadata()](reportablemetadata().md)
  Automatically generates `ReportableMetadata` conformance for a type.
- [macro ReportableMetadataIgnored()](reportablemetadataignored().md)
  Excludes a property from the generated `metadataDictionary`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/statereporting/reportablemetadatakey(_:))*