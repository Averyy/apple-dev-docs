# assetInstallationRequest(supporting:)

**Framework**: Speech  
**Kind**: method

Returns an `AssetsInstallationRequest` object, which is used to initiate the asset download and monitor the progress.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static func assetInstallationRequest(supporting modules: [any SpeechModule]) async throws -> AssetInstallationRequest?
```

#### Discussion

If the current status is `.installed`, returns nil, indicating that nothing further needs to be done.

If some of the assets require locales that aren’t allocated, it automatically allocates those locales. If that would exceed [`maximumAllocatedLocales`](assetinventory/maximumallocatedlocales.md), then it throws an error.

If the assets are not supported, the request object will throw an error.

## See Also

- [static func allocate(locale: Locale) async throws -> Bool](assetinventory/allocate(locale:).md)
  Adds the locale to `allocatedLocales`. Throws if the number of locales would exceed `maximumAllocatedLocales`. Returns false if the locale is already in the set.
- [static func deallocate(locale: Locale) async -> Bool](assetinventory/deallocate(locale:).md)
  Removes the locale from `allocatedLocales`. Returns false if the locale is not in the set.
- [static func status(forModules: [any SpeechModule]) async -> AssetInventory.Status](assetinventory/status(formodules:).md)
  Returns the status for the list of modules. If the status differs between modules, it returns the lowest status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinventory/assetinstallationrequest(supporting:))*