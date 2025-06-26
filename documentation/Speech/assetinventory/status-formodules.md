# status(forModules:)

**Framework**: Speech  
**Kind**: method

Returns the status for the list of modules. If the status differs between modules, it returns the lowest status.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static func status(forModules modules: [any SpeechModule]) async -> AssetInventory.Status
```

## See Also

- [static func allocate(locale: Locale) async throws -> Bool](assetinventory/allocate(locale:).md)
  Adds the locale to `allocatedLocales`. Throws if the number of locales would exceed `maximumAllocatedLocales`. Returns false if the locale is already in the set.
- [static func assetInstallationRequest(supporting: [any SpeechModule]) async throws -> AssetInstallationRequest?](assetinventory/assetinstallationrequest(supporting:).md)
  Returns an `AssetsInstallationRequest` object, which is used to initiate the asset download and monitor the progress.
- [static func deallocate(locale: Locale) async -> Bool](assetinventory/deallocate(locale:).md)
  Removes the locale from `allocatedLocales`. Returns false if the locale is not in the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinventory/status(formodules:))*