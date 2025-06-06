# TN3177: Understanding alternate audio track groups in movie files

**Framework**: Technotes

Learn how alternate groups collect audio tracks, and how to choose which audio track to use in your app.

#### Overview

Movies recorded in QuickTime Movie files and MPEG-4 files by the Camera app on iPhone 16 and iPhone 16 Pro, and by spatial video captures on Apple Vision Pro, may have more than one audio track, containing the same recording in different formats. One track carries Spatial Audio and the other serves as a stereo fallback.

Movie files collect these tracks into [`Preparing sound and subtitle alternate groups for use with Apple devices`](https://developer.apple.com/documentation/QuickTime-File-Format/Preparing_sound_and_subtitle_alternate_groups_for_use_with_Apple_devices), from which at most one track should be used at a time.

#### Alternate Groups

Movies use [`Preparing sound and subtitle alternate groups for use with Apple devices`](https://developer.apple.com/documentation/QuickTime-File-Format/Preparing_sound_and_subtitle_alternate_groups_for_use_with_Apple_devices) to describe multiple language audio tracks and subtitle tracks. Alternate groups can also indicate the relationship between stereo and surround audio tracks when they are recordings of the same audio source: only one should be played at a time.

A track association (also called a track reference) can indicate that the stereo track is a  for the surround track. In general, the older and more compatible formats are fallbacks for the newer and more sophisticated formats.

The iPhone 16 series and Apple Vision Pro use a similar approach when capturing Spatial Audio, writing QuickTime Movie files with an alternate group containing:

- a stereo AAC track, and
- a Spatial Audio track.

The stereo track is associated as the fallback track for the Spatial Audio track.

> ❗ **Important**: If your app examines or uses audio tracks directly, it should honor the relationship between tracks in an alternate group, and use no more than one track from any alternate group at one time. If you mix audio from different tracks in the same group, your app will produce incorrect audio.

#### Enabled Tracks

When you use [`AVAsset`](https://developer.apple.com/documentation/AVFoundation/AVAsset) APIs to access tracks in a movies, each track in the asset reports an `isEnabled` property telling you whether the track is marked in the movie file as enabled or disabled.

For alternate groups, at most one of the tracks will be marked as enabled, indicating a default or expected track in the group. All other tracks in the group will be marked as disabled.

In the case of alternate groups with a Spatial Audio track, the stereo track is marked enabled, and the Spatial Audio track is marked disabled.

![AVAsset tracks](https://docs-assets.developer.apple.com/published/af2ba164304df4151d641baae2e6aed9/tn3177-avasset-tracks.png)

If your app examines or uses audio tracks directly, and you have no other specific processing requirements, you can simply skip disabled tracks. To test whether a track is enabled or disabled, use [`load(_:)`](https://developer.apple.com/documentation/AVFoundation/AVAsynchronousKeyValueLoading/load(_:)):

```None
for track in try await asset.loadTracks(withMediaType: .audio) {
    if try await track.load(.isEnabled) {
        //...
    }
}
```

To query alternate track groups, use the [`trackGroups`](https://developer.apple.com/documentation/AVFoundation/AVPartialAsyncProperty/trackGroups) property.

> ❗ **Important**: If your app currently iterates over audio tracks for custom processing without taking notice of whether the tracks are enabled or disabled, you should update it to do so.

> **Note**: [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) uses a more sophisticated strategy. It automatically enables the audio track appropriate for the current audio route and disables the others.

#### Enabled State in Movie File Tracks

When you’re using [`AVFoundation`](https://developer.apple.com/documentation/AVFoundation), you can rely on its APIs for parsing and writing movie files.

If you have reasons to implement parsing and writing yourself, you’ll need to understand where to find the enabled and alternate group state of tracks in the movie file format, whether [`QuickTime File Format`](https://developer.apple.com/documentation/quicktime-file-format) or ISO Base Media File Format (`ISOBMFF`) (ISO/IEC 14496-12:2020).

> **Note**: `MP4` files are the best known member of the `ISOBMFF` family.

QuickTime Movie and `ISOBMFF` files both carry audiovisual media. The QuickTime File Format and `ISOBMFF` are very similar, as the latter was based upon the former. The format organization of QuickTime Movie files uses structures called “atoms”. `ISOBMFF` files uses many of the same structures but calls them “boxes”. You can find descriptions of “Track atom” and “TrackBox”, for instance, by reading the respective specifications.

In QuickTime Movie files, the enabled state of a QuickTime Movie track is stored as a single bit flag (`0x000001`) in the 3-byte `Flags` field of the [`Track header atom ('tkhd')`](https://developer.apple.com/documentation/quicktime-file-format/Track_header_atom). In the QuickTime File Format specification this flag is called [`Flags`](https://developer.apple.com/documentation/quicktime-file-format/Track_header_atom/Flags). If this bit is set to `1`, the track is enabled. Otherwise, when it is `0`, the track is disabled.

For MPEG-4 (or more generally `ISOBMFF`) files, the enabled state is carried in the 3-byte `flags` field of the `TrackHeaderBox`. The `track_enabled` flag (`0x000001`) is used to mark the track as enabled. A value of `0` in this position disables the track.

#### Alternate Group State in Movie File Tracks

Each movie track can optionally be associated with an alternate group. Typically, only tracks of a particular kind or category will be in the same alternate group. For example, one alternate group might contain only audio tracks. Another alternate group might contain only subtitle or closed caption tracks.

A track’s alternate group is signaled using a 16-bit integer used to associate tracks.

- In QuickTime Movie files, the [`Track header atom ('tkhd')`](https://developer.apple.com/documentation/quicktime-file-format/Track_header_atom) carries a 16-bit integer [`Alternate group`](https://developer.apple.com/documentation/quicktime-file-format/Track_header_atom/Alternate_group) field.
- In `ISOBMFF`, the `TrackHeaderBox` `ISOBMFF` carries a 16-bit integer `alternate_group` field.

A value of `0` indicates the track is not a member of an alternate group. A non-zero value in one track can be matched to the same value in other tracks to identify alternate group membership.

> **Note**: If more than one audio or video track is present in an alternate group, their `track_enabled` flags, as described above, indicate the default choice of track from the group to be presented. The ordering of their serialization in the file should not be considered significant.

#### Revision History

-  First published.

## See Also

- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.
- [TN3183: Adding required reason API entries to your privacy manifest](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest.md)
  Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.
- [TN3184: Adding data collection details to your privacy manifest](tn3184-adding-data-collection-details-to-your-privacy-manifest.md)
  Declare the data your app or third-party SDK collects in a privacy manifest.
- [TN3181: Debugging an invalid privacy manifest](tn3181-debugging-invalid-privacy-manifest.md)
  Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.
- [TN3180: Reverting to App Store Server Notifications V1](tn3180-reverting-app-store-server-notifications-v1.md)
  Migrate from version 2 to version 1 of App Store Server Notifications using the Modify an App endpoint.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3178: Checking for and resolving build UUID problems](tn3178-checking-for-and-resolving-build-uuid-problems.md)
  Ensure that every Mach-O image has a UUID, and that every distinct Mach-O image has its own unique UUID.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3176: Troubleshooting Apple Pay payment processing issues](tn3176-troubleshooting-apple-pay-payment-processing-issues.md)
  Diagnose errors that occur when processing Apple Pay payments, identify common causes, and explore potential solutions.
- [TN3175: Diagnosing issues with displaying the Apple Pay button on your website](tn3175-diagnosing-issues-with-displaying-the-apple-pay-button-on-your-website.md)
  Diagnose common errors received while displaying the Apple Pay button on your website by identifying the underlying causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Technotes/tn3177-understanding-alternate-audio-track-groups-in-movie-files)*