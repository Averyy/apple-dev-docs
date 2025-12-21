# MigrationRequest

**Framework**: AppMigrationKit  
**Kind**: typealias

A migration request that uses the default supported options.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
typealias MigrationRequest = MigrationRequestWithOptions<MigrationDefaultSupportedOptions>
```

#### Discussion

This type alias is a [`MigrationRequestWithOptions`](migrationrequestwithoptions.md) with the `OptionsType` generic constraint [`MigrationDefaultSupportedOptions`](migrationdefaultsupportedoptions.md). Use this type of request for migrations that don’t need to incorporate any options specific to the counterpart operating system.

## See Also

- [struct MigrationRequestWithOptions](migrationrequestwithoptions.md)
  An object that exposes properties of the migration request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/migrationrequest)*