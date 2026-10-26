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

> **Deprecated**: INNoteContentResolutionResult is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class func disambiguation(with noteContentsToDisambiguate: [INNoteContent]) -> Self
```

```objc
+ (instancetype) disambiguationWithNoteContentsToDisambiguate:(NSArray<INNoteContent *> *) noteContentsToDisambiguate;
```

#### Return Value

A new [`INNoteContentResolutionResult`](../innotecontentresolutionresult.md) object.

#### Discussion

Use this method to create a result object when more than one note matches the provided information and you cannot pick one definitively. Ask the user to select from among the notes that you specify.

## Parameters

- `noteContentsToDisambiguate`: An array of [`INNoteContent`](../innotecontent.md) objects for the user to choose from.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INNoteContent) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: INNoteContent?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires confirmation from the user before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/innotecontentresolutionresult/disambiguation(with:))*