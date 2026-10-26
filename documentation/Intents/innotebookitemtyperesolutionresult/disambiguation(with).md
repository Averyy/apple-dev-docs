# disambiguation(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires the user to select from among the specified objects.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- watchOS 4.0+

## Declaration

```swift
@nonobjc
static func disambiguation(with notebookItemTypesToDisambiguate: [INNotebookItemType]) -> Self
```

#### Return Value

A new [`INNotebookItemTypeResolutionResult`](../innotebookitemtyperesolutionresult.md) object.

#### Discussion

Use this method to create a result object when more than one notebook item type matches the given information and you cannot pick one definitively. Ask the user to select from among the item types that you specify.

## Parameters

- `notebookItemTypesToDisambiguate`: An array of [`INNotebookItemType`](../innotebookitemtype.md) values for the user to choose from.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INNotebookItemType) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: INNotebookItemType) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires confirmation from the user before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/innotebookitemtyperesolutionresult/disambiguation(with:))*