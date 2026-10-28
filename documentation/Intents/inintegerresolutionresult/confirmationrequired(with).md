# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires that the user must confirm the value before proceeding.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 11.0+
- tvOS 14.0+
- watchOS 3.2+

## Declaration

```swift
@nonobjc
static func confirmationRequired(with valueToConfirm: Int?) -> Self
```

## Return Value

A new [`INIntegerResolutionResult`](../inintegerresolutionresult.md) object.

## Discussion

Use this method when you can resolve the property to a single value but want the user to confirm that value.

## Parameters

- `valueToConfirm`: The value that resolves the request but that must be confirmed by the user.

## See Also

### Creating a Resolution Result Object
- [class func success(with: Int) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inintegerresolutionresult/confirmationrequired(with:))*