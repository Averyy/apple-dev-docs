# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object with a resolution that requires the user to confirm the value before proceeding.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class func confirmationRequired(with outgoingMessageTypeToConfirm: INOutgoingMessageType) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithOutgoingMessageTypeToConfirm:(INOutgoingMessageType) outgoingMessageTypeToConfirm;
```

#### Return Value

A new [`INOutgoingMessageTypeResolutionResult`](../inoutgoingmessagetyperesolutionresult.md) object.

## Parameters

- `outgoingMessageTypeToConfirm`: A message type for the user to accept or reject.

## See Also

### Creating a Resolution Result
- [class func success(with: INOutgoingMessageType) -> Self](./success%28with%29.md)
  Creates an object with a resolution that involves the successful matching of the specified parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inoutgoingmessagetyperesolutionresult/confirmationrequired(with:))*