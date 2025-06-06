# CapturedRoom.ModelProvider.Error.attributeCombinationNotSupported

**Framework**: RoomPlan  
**Kind**: case

An error that indicates the framework doesn’t support the attributes set in a model-URL query.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
case attributeCombinationNotSupported
```

#### Discussion

This error occurs for the [`modelFileURL(for:)`](capturedroom/modelprovider/modelfileurl(for:)-58ykp.md) function when an unsupported combination of attributes resides in the argument array.

## See Also

- [CapturedRoom.ModelProvider.Error.nonExistingFile(url:)](capturedroom/modelprovider/error/nonexistingfile(url:).md)
  An error that indicates a model-URL query failed to return a result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/modelprovider/error/attributecombinationnotsupported)*