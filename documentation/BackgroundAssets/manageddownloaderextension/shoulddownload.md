# shouldDownload(_:)

**Framework**: Background Assets  
**Kind**: method  
**Required**: Yes

Determines whether a particular asset pack should be downloaded.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func shouldDownload(_ assetPack: AssetPack) -> Bool
```

#### Return Value

Whether the asset pack should be downloaded.

#### Discussion

By default, the system automatically downloads all applicable asset packs with either “essential” or “prefetch” download policies for the current installation event type. You can optionally implement this method to filter out unwanted asset packs at runtime.

## Parameters

- `assetPack`: An asset pack that’s being considered as a candidate to be downloaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/manageddownloaderextension/shoulddownload(_:))*