# shouldDownload(_:)

**Framework**: Background Assets  
**Kind**: method  
**Required**: Yes

Determines whether to download an asset pack.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func shouldDownload(_ assetPack: AssetPack) -> Bool
```

## Mentions

- [Downloading Apple-hosted asset packs](downloading-apple-hosted-asset-packs.md)

#### Return Value

Whether the asset pack should be downloaded.

#### Discussion

By default, the system automatically downloads all applicable asset packs with either “essential” or “prefetch” download policies for the current installation event type. You can optionally implement this method to filter out unwanted asset packs at runtime.

## Parameters

- `assetPack`: An asset pack that’s being considered as a candidate to be downloaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/manageddownloaderextension/shoulddownload(_:))*