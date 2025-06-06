# CapturedRoom.ModelProvider.Error.nonExistingFile(url:)

**Framework**: RoomPlan  
**Kind**: case

An error that indicates a model-URL query failed to return a result.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
case nonExistingFile(url: URL)
```

#### Discussion

This error occurs when the app hasn’t associated a URL to the attributes in a model-URL query.

## Parameters

- `URL`: The URL that references a nonexisting file.

## See Also

- [CapturedRoom.ModelProvider.Error.attributeCombinationNotSupported](capturedroom/modelprovider/error/attributecombinationnotsupported.md)
  An error that indicates the framework doesn’t support the attributes set in a model-URL query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/modelprovider/error/nonexistingfile(url:))*