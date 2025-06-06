# ContentFailure

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

An object that describes why the client can’t play a specific piece of content.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object ContentFailure
```

#### Discussion

The value of `errorCode` is one of the following:

| Code | Description |
| --- | --- |
| `0` | The client encountered an unexpected error. |
| `1000` | The number of items in the queue segment exceeds the configured maximum. For more information, see [`Constraints`](constraints.md). |
| `1001` | The client failed to play the specified item. For more information, see [`UnderlyingError`](underlyingerror.md). |
| `1002` | The client failed to obtain a content key for a protected item. |

If you receive a [`ContentFailure`](contentfailure.md) with an `errorCode` of `1002`, check the following:

- The configuration for your service’s certificate URL is correct. For more information, see [`ExtensionConfig.Media.Queues.ContentProtectionKey.Cks`](extensionconfig/media-data.dictionary/queues-data.dictionary/contentprotectionkey-data.dictionary/cks-data.dictionary.md).
- The protected item has a valid `assetIdentifier`.
- Your service’s key server module (KSM) provides a valid content key context (CKC) for the protected item’s `assetIdentifier`. For more information, see [`FairPlay Streaming Overview`](https://developer.apple.comhttps://developer.apple.com/streaming/fps/FairPlayStreamingOverview.pdf).

> **Note**:  The client doesn’t send an error if your service provides an invalid content key for the specified `assetIdentifier`.

 The client doesn’t send an error if your service provides an invalid content key for the specified `assetIdentifier`.

## See Also

- [Recover from Content Playback Failure](contentplaybackfailure.md)
  Provide a recovery queue that allows the client to resume playback after an error.
- [object ContentPlaybackFailureRequest](contentplaybackfailurerequest.md)
  A request the client sends to recover from failed content playback.
- [object ContentPlaybackFailureResponse](contentplaybackfailureresponse.md)
  A response that allows the client to recover from failed content playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/contentfailure)*