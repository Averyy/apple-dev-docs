# PHAssetEditOperation.setLivePhotoVideoPlaybackEnabled

**Framework**: Photos  
**Kind**: case  
**Role**: Case

Whether Live Photo video playback can be enabled or disabled for the asset.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
case setLivePhotoVideoPlaybackEnabled
```

```c
PHAssetEditOperationSetLivePhotoVideoPlaybackEnabled
```

## Discussion

If true, use [`setLivePhotoVideoPlaybackEnabled(_:)`](../phassetchangerequest/setlivephotovideoplaybackenabled%28_%29.md) to change the setting. This is false for an asset that is not a Live Photo, or a Live Photo whose video was hidden by an edit without a paired video (that video cannot be restored without discarding the edit)


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phasseteditoperation/setlivephotovideoplaybackenabled)*