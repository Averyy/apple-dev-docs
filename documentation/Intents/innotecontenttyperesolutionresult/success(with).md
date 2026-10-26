# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves the successful matching of the specified parameter.

**Availability**:
- iOS 11.0+ - Deprecated in 13.0
- iPadOS 11.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 6.0

> **Deprecated**: This resolution result is no longer used

## Declaration

```swift
class func success(with resolvedNoteContentType: INNoteContentType) -> Self
```

```objc
+ (instancetype) successWithResolvedNoteContentType:(INNoteContentType) resolvedNoteContentType;
```

#### Return Value

A new [`INNoteContentTypeResolutionResult`](../innotecontenttyperesolutionresult.md) object.

#### Discussion

Use this method to create a result object when you support the specified type of content.

## Parameters

- `resolvedNoteContentType`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INNoteContentType) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires confirmation from the user before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/innotecontenttyperesolutionresult/success(with:))*