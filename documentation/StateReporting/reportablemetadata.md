# ReportableMetadata()

**Framework**: StateReporting  
**Kind**: macro

Automatically generates `ReportableMetadata` conformance for a type.

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
(member, names: named(metadataDictionary)) @attached(extension, conformances: ReportableMetadata) macro ReportableMetadata()
```

## Mentions

- [Getting started with StateReporting](getting-started-with-statereporting.md)

#### Overview

Apply `@ReportableMetadata` to a `struct` or `class` to enable generation of a `metadataDictionary` from its stored properties. Properties with supported types (`String`, `Int`, `Double`, `Date`, `Bool`) are included; properties with unsupported types are silently skipped. The macro generates a `metadataDictionary` that maps each included property name to the corresponding [`ReportableMetadataValue`](reportablemetadatavalue.md) case.

Use [`ReportableMetadataKey(_:)`](reportablemetadatakey(_:).md) to override the dictionary key for a specific property, and [`ReportableMetadataIgnored()`](reportablemetadataignored().md) to exclude a property entirely.

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

- [macro ReportableMetadataKey(String)](reportablemetadatakey(_:).md)
  Specifies a custom key name for a property in the generated `metadataDictionary`.
- [macro ReportableMetadataIgnored()](reportablemetadataignored().md)
  Excludes a property from the generated `metadataDictionary`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/statereporting/reportablemetadata())*