# Offline playback and storage

**Framework**: AVFoundation

Download streamed content to disk to allow offline playback, and define policies to automatically remove downloaded assets.

## Topics

### Asset downloading
- [Using AVFoundation to play and persist HTTP Live Streams](using-avfoundation-to-play-and-persist-http-live-streams.md)
  Play HTTP Live Streams and persist streams on disk for offline playback using AVFoundation.
- [class AVAssetDownloadURLSession](avassetdownloadurlsession.md)
  A URL session that creates and executes asset download tasks.
- [class AVAssetDownloadTask](avassetdownloadtask.md)
  A session used to download HTTP Live Streaming assets.
- [class AVAggregateAssetDownloadTask](avaggregateassetdownloadtask.md)
  A task that downloads multiple media selections for an asset.
### Offline storage management
- [class AVAssetDownloadStorageManager](avassetdownloadstoragemanager.md)
  An object that manages policies to automatically purge downloaded assets.
- [class AVAssetDownloadStorageManagementPolicy](avassetdownloadstoragemanagementpolicy.md)
  An object that defines a policy to automatically manage the storage of downloaded assets.
- [class AVMutableAssetDownloadStorageManagementPolicy](avmutableassetdownloadstoragemanagementpolicy.md)
  A mutable object that you use to create a new storage management policy.
### Cache monitoring
- [class AVAssetCache](avassetcache.md)
  An object that you use to inspect locally cached media data.

## See Also

- [Media playback](media-playback.md)
  Manage the playback of media assets and interstitial content, independent of how you present that content in your interface.
- [Streaming and AirPlay](streaming-and-airplay.md)
  Stream content wirelessly to other devices using AirPlay, and handle requests involving FairPlay-protected assets.
- [Sample buffer playback](sample-buffer-playback.md)
  Create custom controllers to play and synchronize the timing of sample buffer streams.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/offline-playback-and-storage)*