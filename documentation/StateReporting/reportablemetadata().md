# ReportableMetadata()

**Framework**: StateReporting  
**Kind**: macro  
**Role**: Macro

Automatically generates `ReportableMetadata` conformance for a type.

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
@attached(member, names: named(metadataDictionary))
@attached(extension, conformances: ReportableMetadata) macro ReportableMetadata()
```

## Mentions

- [Getting started with StateReporting](./getting-started-with-statereporting.md)

## Overview

Apply `@ReportableMetadata` to a `struct` or `class` to enable generation of a `metadataDictionary` from its stored properties. Properties with supported types (`String`, `Int`, `Double`, `Date`, `Bool`) are included; properties with unsupported types are silently skipped. The macro generates a `metadataDictionary` that maps each included property name to the corresponding [`ReportableMetadataValue`](./reportablemetadatavalue.md) case.

Use [`ReportableMetadataKey(_:)`](./reportablemetadatakey%28_%29.md) to override the dictionary key for a specific property, and [`ReportableMetadataIgnored()`](./reportablemetadataignored%28%29.md) to exclude a property entirely.

```swift
@ReportableMetadata
struct CheckoutMetadata {
    var cartItemCount: Int
    var promoCode: String?
    @ReportableMetadataKey("ts") var timestamp: Date
    @ReportableMetadataIgnored var internalToken: String
}
```

## See Also

### Metadata type macros
- [macro ReportableMetadataKey(String)](./reportablemetadatakey%28_%29.md)
  Specifies a custom key name for a property in the generated `metadataDictionary`.
- [macro ReportableMetadataIgnored()](./reportablemetadataignored%28%29.md)
  Excludes a property from the generated `metadataDictionary`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/statereporting/reportablemetadata())*