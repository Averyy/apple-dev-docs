# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires confirmation from the user before proceeding.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INNotebookItemTypeResolutionResult is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class func confirmationRequired(with notebookItemTypeToConfirm: INNotebookItemType) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithNotebookItemTypeToConfirm:(INNotebookItemType) notebookItemTypeToConfirm;
```

#### Return Value

A new [`INNotebookItemTypeResolutionResult`](../innotebookitemtyperesolutionresult.md) object.

#### Discussion

Use this method when you cannot search for the specified type of content but can search for a similar type and want to confirm with the user before proceeding.

## Parameters

- `notebookItemTypeToConfirm`: The value that resolves the request but must be confirmed by the user.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INNotebookItemType) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [static func disambiguation(with: [INNotebookItemType]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/innotebookitemtyperesolutionresult/confirmationrequired(with:))*