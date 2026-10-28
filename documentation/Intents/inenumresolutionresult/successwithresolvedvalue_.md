# successWithResolvedValue:

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves the successful matching of the specified parameter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
+ (instancetype) successWithResolvedValue:(NSInteger) resolvedValue;
```

## Return Value

A new [`INEnumResolutionResult`](../inenumresolutionresult.md) object.

## Discussion

Use this method to create a result object when you can resolve a parameter successfully to a value in your own internal data structures.

## Parameters

- `resolvedValue`: The object that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Type Methods
- [+ confirmationRequiredWithValueToConfirm:](./confirmationrequiredwithvaluetoconfirm_.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inenumresolutionresult/successwithresolvedvalue:)*