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

> **Deprecated**: INNotebookItemTypeResolutionResult is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class func success(with resolvedNotebookItemType: INNotebookItemType) -> Self
```

```objc
+ (instancetype) successWithResolvedNotebookItemType:(INNotebookItemType) resolvedNotebookItemType;
```

## Return Value

A new [`INNotebookItemTypeResolutionResult`](../innotebookitemtyperesolutionresult.md) object.

## Discussion

Use this method to create a result object when you support searching for the specified type of content.

## Parameters

- `resolvedNotebookItemType`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INNotebookItemType) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires confirmation from the user before proceeding.
- [static func disambiguation(with: [INNotebookItemType]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.
- [+ disambiguationWithNotebookItemTypesToDisambiguate:](./disambiguationwithnotebookitemtypestodisambiguate_.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/innotebookitemtyperesolutionresult/success(with:))*