# ManagedDownloaderExtension

**Framework**: Background Assets  
**Kind**: protocol

A protocol to which a managed downloader extension must conform.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol ManagedDownloaderExtension : BADownloaderExtension where Self.Configuration : ManagedDownloaderExtensionConfiguration
```

#### Overview

The protocol provides default implementations for all of the inherited `BADownloaderExtension` requirements.

> ⚠️ **Warning**: Don’t implement any of the inherited `BADownloaderExtension` requirements aside from, optionally, [`backgroundDownload(_:didReceive:)`](badownloaderextension-qwaw/backgrounddownload(_:didreceive:).md).

## Topics

### Instance Methods
- [func shouldDownload(AssetPack) -> Bool](manageddownloaderextension/shoulddownload(_:).md)
  Determines whether a particular asset pack should be downloaded.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)
- [BADownloaderExtension](badownloaderextension-qwaw.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/manageddownloaderextension)*