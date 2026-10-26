# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves successfully matching the specified parameter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func success(with resolvedMediaAffinityType: INMediaAffinityType) -> Self
```

```objc
+ (instancetype) successWithResolvedMediaAffinityType:(INMediaAffinityType) resolvedMediaAffinityType;
```

#### Return Value

A new [`INMediaAffinityTypeResolutionResult`](../inmediaaffinitytyperesolutionresult.md) object.

#### Discussion

Use this method to create a result object when you’re able to update the user’s affinity for the media item.

## Parameters

- `resolvedMediaAffinityType`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result
- [class func confirmationRequired(with: INMediaAffinityType) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediaaffinitytyperesolutionresult/success(with:))*