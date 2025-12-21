# OptionsType

**Framework**: AppMigrationKit  
**Kind**: associatedtype  
**Required**: Yes

A type that indicates the options supported by the destination device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
associatedtype OptionsType : CaseIterable, Hashable, RawRepresentable, Sendable where Self.OptionsType.RawValue == String
```

#### Discussion

This type defines the [`options`](migrationrequestwithoptions/options.md) of the export’s [`MigrationRequestWithOptions`](migrationrequestwithoptions.md). If you don’t need a unique type for export options, your app extension can conform to [`ResourcesExporting`](resourcesexporting.md) instead, which uses [`MigrationDefaultSupportedOptions`](migrationdefaultsupportedoptions.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/resourcesexportingwithoptions/optionstype)*