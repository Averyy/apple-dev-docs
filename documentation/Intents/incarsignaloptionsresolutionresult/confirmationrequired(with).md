# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates a resolution object that requires confirmation of the provided value.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func confirmationRequired(with carSignalOptionsToConfirm: INCarSignalOptions = []) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithCarSignalOptionsToConfirm:(INCarSignalOptions) carSignalOptionsToConfirm;
```

## Return Value

A new `INCarSignalOptionsResolutionResult` object.

## Discussion

Use this method when you can resolve the parameter to the specified value, but you still want the user to confirm that value.

## Parameters

- `carSignalOptionsToConfirm`: The signal option value to confirm. For a list of possible values, see [`INCarSignalOptions`](../incarsignaloptions.md).

## See Also

### Creating a Resolution Result Object
- [class func success(with: INCarSignalOptions) -> Self](./success%28with%29.md)
  Creates a resolution object that indicates the successful resolution of the provided value.
- [+ successWithResolvedValue:](./successwithresolvedvalue_.md)
- [+ confirmationRequiredWithValueToConfirm:](./confirmationrequiredwithvaluetoconfirm_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incarsignaloptionsresolutionresult/confirmationrequired(with:))*