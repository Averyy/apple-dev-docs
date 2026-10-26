# downloadOfAssetPack:hasProgress:

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Notifies the receiver that the download is in progress.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (void) downloadOfAssetPack:(BAAssetPack *) assetPack hasProgress:(NSProgress *) progress;
```

## Parameters

- `assetPack`: The asset pack.
- `progress`: The download progress.

## See Also

### Tracking downloads
- [- downloadOfAssetPackBegan:](./downloadofassetpackbegan_.md)
  Notifies the receiver that the download began or resumed after being paused.
- [- downloadOfAssetPackPaused:](./downloadofassetpackpaused_.md)
  Notifies the receiver that the download paused.
- [- downloadOfAssetPackFinished:](./downloadofassetpackfinished_.md)
  Notifies the receiver that the download completed and that the asset pack is available locally.
- [- downloadOfAssetPack:failedWithError:](./downloadofassetpack_failedwitherror_.md)
  Notifies the receiver that the download failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/bamanagedassetpackdownloaddelegate/downloadofassetpack:hasprogress:)*