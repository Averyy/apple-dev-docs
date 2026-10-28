# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires that the user must confirm the value before proceeding.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func confirmationRequired(with mediaAffinityTypeToConfirm: INMediaAffinityType) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithMediaAffinityTypeToConfirm:(INMediaAffinityType) mediaAffinityTypeToConfirm;
```

## Return Value

A new [`INMediaAffinityTypeResolutionResult`](../inmediaaffinitytyperesolutionresult.md) object.

## Discussion

Use this method when you can’t resolve the parameter to an affinity that’s similar, but not equal to, the one specified in the intent. Don’t use this method to resolve affinities your app doesn’t support.

## Parameters

- `mediaAffinityTypeToConfirm`: The value that resolves the request but must be confirmed by the user.

## See Also

### Creating a Resolution Result
- [class func success(with: INMediaAffinityType) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves successfully matching the specified parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediaaffinitytyperesolutionresult/confirmationrequired(with:))*