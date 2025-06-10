# StoreDownloaderExtension

**Framework**: StoreKit  
**Kind**: protocol

A protocol to which a downloader extension for Apple-Hosted Background Assets must conform.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol StoreDownloaderExtension : ManagedDownloaderExtension
```

#### Overview

The protocol provides default implementations for all of the inherited `BADownloaderExtension` requirements. You can optionally implement the inherited `ManagedDownloaderExtension` requirements. For more information, see [`Background Assets`](https://developer.apple.com/documentation/BackgroundAssets).

> ⚠️ **Warning**: Don’t implement any of the inherited `BADownloaderExtension` requirements.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)
- [BADownloaderExtension](../BackgroundAssets/BADownloaderExtension-qwaw.md)
- [ManagedDownloaderExtension](../BackgroundAssets/ManagedDownloaderExtension.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storedownloaderextension)*