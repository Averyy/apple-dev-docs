# success(with:)

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

```swift
class func success(with resolvedTimeInterval: TimeInterval) -> Self
```

```objc
+ (instancetype) successWithResolvedTimeInterval:(NSTimeInterval) resolvedTimeInterval;
```

#### Return Value

A new [`INTimeIntervalResolutionResult`](../intimeintervalresolutionresult.md) object.

#### Discussion

Use this method to create a result object when you can resolve a parameter successfully to a value in your own internal data structures.

## Parameters

- `resolvedTimeInterval`: The object that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result
- [class func confirmationRequired(with: TimeInterval) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intimeintervalresolutionresult/success(with:))*