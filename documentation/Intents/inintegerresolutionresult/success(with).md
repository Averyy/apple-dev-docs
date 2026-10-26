# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves the successful matching of the specified value.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func success(with resolvedValue: Int) -> Self
```

```objc
+ (instancetype) successWithResolvedValue:(NSInteger) resolvedValue;
```

#### Return Value

A new [`INIntegerResolutionResult`](../inintegerresolutionresult.md) object.

#### Discussion

Use this method to create a result object when you are able to resolve a parameter successfully to a value in your own internal data structures.

## Parameters

- `resolvedValue`: The value that resolves the requested property of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [static func confirmationRequired(with: Int?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inintegerresolutionresult/success(with:))*