# SKDownloaderExtension

**Framework**: StoreKit  
**Kind**: protocol  
**Role**: Protocol

An application extension that uses the system implementation to schedule Apple-hosted asset-pack downloads automatically.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
@protocol SKDownloaderExtension <BAManagedDownloaderExtension>
```

## Overview

You can optionally implement the inherited `BAManagedDownloaderExtension` requirements, but don’t implement any of the inherited `BADownloaderExtension` requirements. For more information, see [Background Assets](../BackgroundAssets/BackgroundAssets.md).

## Relationships

### Inherits From
- [BAManagedDownloaderExtension](../BackgroundAssets/bamanageddownloaderextension.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skdownloaderextension)*