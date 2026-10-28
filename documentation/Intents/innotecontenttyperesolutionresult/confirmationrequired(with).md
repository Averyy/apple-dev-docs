# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires confirmation from the user before proceeding.

**Availability**:
- iOS 11.0+ - Deprecated in 13.0
- iPadOS 11.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 6.0

> **Deprecated**: This resolution result is no longer used

## Declaration

```swift
class func confirmationRequired(with noteContentTypeToConfirm: INNoteContentType) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithNoteContentTypeToConfirm:(INNoteContentType) noteContentTypeToConfirm;
```

## Return Value

A new [`INNoteContentTypeResolutionResult`](../innotecontenttyperesolutionresult.md) object.

## Discussion

Use this method when you cannot provide note content for the specified type but can provide it for a different type and want to confirm with the user before proceeding.

## Parameters

- `noteContentTypeToConfirm`: The value that resolves the request but must be confirmed by the user.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INNoteContentType) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/innotecontenttyperesolutionresult/confirmationrequired(with:))*