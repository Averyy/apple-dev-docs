# AddMediaMediaItemResolutionResult.Unsupported

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary  
**Role**: Object

The reason your service can’t add the media item to the user’s library or to a playlist.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
object AddMediaMediaItemResolutionResult.Unsupported
```

## Discussion

If you can’t find the media item the user specifies, don’t provide a reason. When the client receives an [`AddMediaMediaItemResolutionResult.Unsupported`](./unsupported-data.dictionary.md) object without a reason, the client provides a generic failure message to the user.

## Properties

- `reason` (AddMediaMediaItemUnsupportedReason): The reason your service can’t add the media item to the user’s library or to a playlist.

## See Also

### Reporting a Problem
- [type AddMediaMediaItemUnsupportedReason](../addmediamediaitemunsupportedreason.md)
  Reasons the media service can’t add the media item to the user’s library or to a playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/addmediamediaitemresolutionresult/unsupported-data.dictionary)*