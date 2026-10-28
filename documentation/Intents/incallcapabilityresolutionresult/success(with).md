# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves the successful matching of the specified call capability.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func success(with resolvedCallCapability: INCallCapability) -> Self
```

```objc
+ (instancetype) successWithResolvedCallCapability:(INCallCapability) resolvedCallCapability;
```

## Return Value

A new [`INCallCapabilityResolutionResult`](../incallcapabilityresolutionresult.md) object.

## Discussion

Use this method to create a resolution result object when you recognize the specified type of call capability and are able to use it to resolve an intent.

## Parameters

- `resolvedCallCapability`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INCallCapability) -> Self](./confirmationrequired%28with%29.md)
  Creates a result that asks Siri to verify the request that the user wants to continue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallcapabilityresolutionresult/success(with:))*