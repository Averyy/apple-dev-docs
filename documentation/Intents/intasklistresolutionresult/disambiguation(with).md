# disambiguation(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires the user to select from among the specified objects.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INTaskListResolutionResult is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class func disambiguation(with taskListsToDisambiguate: [INTaskList]) -> Self
```

```objc
+ (instancetype) disambiguationWithTaskListsToDisambiguate:(NSArray<INTaskList *> *) taskListsToDisambiguate;
```

#### Return Value

A new [`INTaskListResolutionResult`](../intasklistresolutionresult.md) object.

#### Discussion

Use this method to create a result object when more than one task list matches the given information and you cannot pick one definitively. Ask the user to select from among the task lists that you specify.

For each [`INTaskList`](../intasklist.md) object that you provide, include enough information to be able to locate that list again later. When the user selects one of the task lists, SiriKit puts the details from your [`INTaskList`](../intasklist.md) object into the intent and asks you to resolve the task list again. Therefore, you might assign a unique value to the [`identifier`](../intasklist/identifier.md) property of the task list so that you can perform a fast lookup of the selected list during the second resolution pass.

## Parameters

- `taskListsToDisambiguate`: An array of [`INTaskList`](../intasklist.md) objects for the user to choose from.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INTaskList) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: INTaskList?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires confirmation from the user before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intasklistresolutionresult/disambiguation(with:))*