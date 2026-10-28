# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates a result that asks Siri to verify the request that the user wants to continue.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func confirmationRequired(with callCapabilityToConfirm: INCallCapability) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithCallCapabilityToConfirm:(INCallCapability) callCapabilityToConfirm;
```

## Return Value

A new [`INCallCapabilityResolutionResult`](../incallcapabilityresolutionresult.md) object.

## Parameters

- `callCapabilityToConfirm`: The value which verifies the user’s request that the user wants to continue.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INCallCapability) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified call capability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallcapabilityresolutionresult/confirmationrequired(with:))*