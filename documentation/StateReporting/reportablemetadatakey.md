# ReportableMetadataKey(_:)

**Framework**: StateReporting  
**Kind**: macro

Specifies a custom key name for a property in the generated `metadataDictionary`.

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