# CapturedRoom.ModelProvider.Error.attributeCombinationNotSupported

**Framework**: RoomPlan  
**Kind**: case  
**Role**: Case

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

This error occurs for the [`modelFileURL(for:)`](../modelfileurl%28for%29-58ykp.md) function when an unsupported combination of attributes resides in the argument array.

## See Also

### Interpreting the error
- [CapturedRoom.ModelProvider.Error.nonExistingFile(url:)](./nonexistingfile%28url%29.md)
  An error that indicates a model-URL query failed to return a result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/modelprovider/error/attributecombinationnotsupported)*