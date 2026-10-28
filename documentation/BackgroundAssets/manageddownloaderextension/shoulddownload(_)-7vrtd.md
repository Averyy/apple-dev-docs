# shouldDownload(_:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Determines whether a particular asset pack should be downloaded.

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

## Return Value

Whether the asset pack should be downloaded.

## Discussion

This default implementation always returns `true`. You can override it to specify your own filtering logic.

## Parameters

- `assetPack`: An asset pack that’s being considered as a candidate to be downloaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/manageddownloaderextension/shoulddownload(_:)-7vrtd)*