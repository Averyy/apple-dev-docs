# StoreDownloaderExtension

**Framework**: StoreKit  
**Kind**: protocol

An app extension that uses the system implementation to schedule Apple-hosted asset-pack downloads automatically.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol StoreDownloaderExtension : ManagedDownloaderExtension
```

#### Overview

You can optionally implement the inherited `ManagedDownloaderExtension` requirements, but don’t implement any of the inherited `BADownloaderExtension` requirements for which this protocol provides a default implementation. For more information, see [`Background Assets`](https://developer.apple.com/documentation/BackgroundAssets).

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)
- [BADownloaderExtension](../BackgroundAssets/BADownloaderExtension-qwaw.md)
- [ManagedDownloaderExtension](../BackgroundAssets/ManagedDownloaderExtension.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storedownloaderextension)*