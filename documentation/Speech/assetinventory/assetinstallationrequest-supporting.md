# assetInstallationRequest(supporting:)

**Framework**: Speech  
**Kind**: method

Returns an installation request object, which is used to initiate the asset download and monitor its progress.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static func assetInstallationRequest(supporting modules: [any SpeechModule]) async throws -> AssetInstallationRequest?
```

#### Discussion

If the current status is `.installed`, returns nil, indicating that nothing further needs to be done.

If some of the assets require locales that aren’t reserved, it automatically reserves those locales. If that would exceed [`maximumReservedLocales`](assetinventory/maximumreservedlocales.md), then it throws an error.

> **Note**: An error if the assets are not supported or no reservations are available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinventory/assetinstallationrequest(supporting:))*