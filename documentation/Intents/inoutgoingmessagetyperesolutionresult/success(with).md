# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object with a resolution that involves the successful matching of the specified parameter.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class func success(with resolvedOutgoingMessageType: INOutgoingMessageType) -> Self
```

```objc
+ (instancetype) successWithResolvedOutgoingMessageType:(INOutgoingMessageType) resolvedOutgoingMessageType;
```

## Return Value

A new [`INOutgoingMessageTypeResolutionResult`](../inoutgoingmessagetyperesolutionresult.md) object.

## Discussion

Use this method to create a result object when you can send a message in the format the intent specifies.

## Parameters

- `resolvedOutgoingMessageType`: The object that resolves the requested parameter of the intent. This value may be different than the one the intent object specifies.

## See Also

### Creating a Resolution Result
- [class func confirmationRequired(with: INOutgoingMessageType) -> Self](./confirmationrequired%28with%29.md)
  Creates an object with a resolution that requires the user to confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inoutgoingmessagetyperesolutionresult/success(with:))*