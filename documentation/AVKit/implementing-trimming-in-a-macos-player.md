# Implementing Trimming in a macOS Player

**Framework**: AVKit

Provide a QuickTime media-trimming experience in your macOS app.

#### Overview

You use [`AVPlayerView`](avplayerview.md) to provide a playback experience like that of QuickTime Player in macOS. However, `AVPlayerView` not only provides the QuickTime playback interface, but it also provides the QuickTime media-trimming experience.

![Single image with multiple video frames selected and Trim button in an enabled state.](https://docs-assets.developer.apple.com/published/773bb33748e3f49024c3fa468360bf25/media-2948756%402x.png)

##### Verify That Trimming Is Allowed

Before attempting to put the player into trimming mode, verify that trimming is allowed by querying the player view’s [`canBeginTrimming`](avplayerview/canbegintrimming.md) property. This property returns `false` if you’re playing an asset delivered over HTTP Live Streaming or if the asset is content protected. If you’re presenting a menu item to initiate trimming, a good place to perform this check is in the [`validateUserInterfaceItem(_:)`](https://developer.apple.com/documentation/AppKit/NSDocument/validateUserInterfaceItem(_:)) method of [`NSDocument`](https://developer.apple.com/documentation/AppKit/NSDocument), so that the menu item can automatically be disabled if trimming is disallowed.

```swift
override func validateUserInterfaceItem(_ item: NSValidatedUserInterfaceItem) -> Bool {
    if item.action == #selector(beginTrimming) {
        return playerView.canBeginTrimming
    }
    return super.validateUserInterfaceItem(item)
}
```

##### Enter Trimming Mode

After you’ve determined that the media supports trimming, you call the [`beginTrimming(completionHandler:)`](avplayerview/begintrimming(completionhandler:).md). This method takes a completion block that you use to determine whether the user completed the trim or canceled the operation.

```swift
@IBAction func beginTrimming(_ sender: AnyObject) {
    playerView.beginTrimming { result in
        if result == .okButton {
            // user selected Trim button (AVPlayerViewTrimResult.okButton)...
        } else {
            // user selected Cancel button (AVPlayerViewTrimResult.cancelButton)...
        }
    }
}
```

##### Transcode the Trimmed Asset

Because [`AVAsset`](https://developer.apple.com/documentation/AVFoundation/AVAsset) is an immutable object, you may be wondering how its duration is changed when you click the Trim button. Trimming relies on a feature of [`AVPlayerItem`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem) to adjust the presented time range. `AVPlayerItem` provides the [`reversePlaybackEndTime`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem/reversePlaybackEndTime) and [`forwardPlaybackEndTime`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem/forwardPlaybackEndTime) properties that set the in and out points for a media item. It doesn’t change the underlying asset, but essentially changes your effective view of it. To save the results of the user’s trim operation, you export a new copy of the asset, trimming it to the specified times. The simplest way to do this is to use [`AVAssetExportSession`](https://developer.apple.com/documentation/AVFoundation/AVAssetExportSession), which provides a simple and performant way for you to transcode the media of an asset. You create a new export session, passing it the asset to export along with a transcoding preset to use.

```swift
// Transcoding preset
let preset = AVAssetExportPresetAppleM4V720pHD
let exportSession = AVAssetExportSession(asset: playerItem.asset, presetName: preset)!
exportSession.outputFileType = AVFileTypeAppleM4V
exportSession.outputURL = // Output URL
```

This example uses a preset to export the media as a 720p, M4V file, but `AVAssetExportSession` supports a wide variety of export presets. To find out what export session presets are supported for the current asset, you can use the session’s [`exportPresets(compatibleWith:)`](https://developer.apple.com/documentation/AVFoundation/AVAssetExportSession/exportPresets(compatibleWith:)) class method, passing it the asset you want to export. This method returns an array of valid presets that you can use in your export.

##### Select the Trimmed Asset

To export only the content the user trimmed, you use the current player item’s reverse and forward end-time values to define a [`CMTimeRange`](https://developer.apple.com/documentation/CoreMedia/CMTimeRange) to set on the export session.

```swift
// Create CMTimeRange with the trim in/out point times
let startTime = self.playerItem.reversePlaybackEndTime
let endTime = self.playerItem.forwardPlaybackEndTime
let timeRange = CMTimeRangeFromTimeToTime(startTime, endTime)
exportSession.timeRange = timeRange
```

##### Export the Trimmed Asset

To perform the actual export operation, you call its [`exportAsynchronously(completionHandler:)`](https://developer.apple.com/documentation/AVFoundation/AVAssetExportSession/exportAsynchronously(completionHandler:)) method. Check the status of the export session in the completion handler and handle completion and failure cases.

```swift
exportSession.exportAsynchronously {
    switch exportSession.status {
    case .completed:
        // Export Complete
    case .failed:
        // failed
    default:
        // handle others
    }
}
```

## See Also

- [class AVPlayerView](avplayerview.md)
  A view that displays content from a player and presents a native user interface to control playback.
- [class AVCaptureView](avcaptureview.md)
  A view that displays standard user interface controls for capturing media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/implementing-trimming-in-a-macos-player)*