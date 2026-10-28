# confirmationRequiredWithValueToConfirm:

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires that the user must confirm the value before proceeding.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
+ (instancetype) confirmationRequiredWithValueToConfirm:(NSInteger) valueToConfirm;
```

## Return Value

A new [`INEnumResolutionResult`](../inenumresolutionresult.md) object.

## Discussion

Use this method when you can resolve the parameter to the specified object but you want the user to confirm that value.

## Parameters

- `valueToConfirm`: The object that resolves the request but must be confirmed by the user.

## See Also

### Type Methods
- [+ successWithResolvedValue:](./successwithresolvedvalue_.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inenumresolutionresult/confirmationrequiredwithvaluetoconfirm:)*