# AddMediaMediaItemResolutionResult.Unsupported

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

The reason your service can’t add the media item to the user’s library or to a playlist.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object AddMediaMediaItemResolutionResult.Unsupported
```

#### Discussion

If you can’t find the media item the user specifies, don’t provide a reason. When the client receives an [`AddMediaMediaItemResolutionResult.Unsupported`](addmediamediaitemresolutionresult/unsupported-data.dictionary.md) object without a reason, the client provides a generic failure message to the user.

## See Also

- [type AddMediaMediaItemUnsupportedReason](addmediamediaitemunsupportedreason.md)
  Reasons the media service can’t add the media item to the user’s library or to a playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/addmediamediaitemresolutionresult/unsupported-data.dictionary)*