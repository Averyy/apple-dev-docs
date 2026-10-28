# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves the successful matching of the specified parameter.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INNoteContentResolutionResult is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class func success(with resolvedNoteContent: INNoteContent) -> Self
```

```objc
+ (instancetype) successWithResolvedNoteContent:(INNoteContent *) resolvedNoteContent;
```

## Return Value

A new [`INNoteContentResolutionResult`](../innotecontentresolutionresult.md) object.

## Discussion

Use this method to create a result object when you are able to identify the specific note content to create or modify.

## Parameters

- `resolvedNoteContent`: The object that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INNoteContent?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires confirmation from the user before proceeding.
- [class func disambiguation(with: [INNoteContent]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/innotecontentresolutionresult/success(with:))*