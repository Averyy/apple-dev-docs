# UpdateMediaAffinityMediaItemResolutionResult.Unsupported

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary  
**Role**: Object

The reason your service can’t update information about the requested media item.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
object UpdateMediaAffinityMediaItemResolutionResult.Unsupported
```

## Properties

- `reason` (UpdateMediaAffinityMediaItemUnsupportedReason): The reason your service can’t update information about the media item.

## See Also

### Specifying the Result
- [object UpdateMediaAffinityMediaItemResolutionResult.Success](./success-data.dictionary.md)
  A media item that successfully matches the intent.
- [object UpdateMediaAffinityMediaItemResolutionResult.Disambiguation](./disambiguation-data.dictionary.md)
  A result that requires the user to choose from multiple media items before proceeding.
- [object UpdateMediaAffinityMediaItemResolutionResult.ConfirmationRequired](./confirmationrequired-data.dictionary.md)
  A result that requires the user to confirm the media item before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/updatemediaaffinitymediaitemresolutionresult/unsupported-data.dictionary)*