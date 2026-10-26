# successWithResolvedValue:

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 4.0

> **Deprecated**: Use [`success(with:)`](./success%28with%29.md) instead.

## Declaration

```objc
+ (instancetype) successWithResolvedValue:(INWorkoutLocationType) resolvedValue;
```

## See Also

### Creating a Resolution Result Object
- [class func success(with: INWorkoutLocationType) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: INWorkoutLocationType) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.
- [+ confirmationRequiredWithValueToConfirm:](./confirmationrequiredwithvaluetoconfirm_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inworkoutlocationtyperesolutionresult/successwithresolvedvalue:)*