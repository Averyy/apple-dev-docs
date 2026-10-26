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

> **Deprecated**: INNoteResolutionResult is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class func disambiguation(with notesToDisambiguate: [INNote]) -> Self
```

```objc
+ (instancetype) disambiguationWithNotesToDisambiguate:(NSArray<INNote *> *) notesToDisambiguate;
```

#### Return Value

A new [`INNoteResolutionResult`](../innoteresolutionresult.md) object.

#### Discussion

Use this method to create a result object when more than one note matches the given information and you can’t pick one definitively. Ask the user to select from among the notes that you specify.

For each [`INNote`](../innote.md) object that you provide, include enough information to be able to locate the note again later. When the user selects one of the notes, SiriKit puts the details from your [`INNote`](../innote.md) object into the intent and asks you to resolve the note again. Therefore, you might assign a unique value to the [`identifier`](../innote/identifier.md) property of the note so that you can perform a fast lookup of the selected note during the second resolution pass.

## Parameters

- `notesToDisambiguate`: An array of [`INNote`](../innote.md) objects for the user to choose from.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INNote) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: INNote?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires confirmation from the user before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/innoteresolutionresult/disambiguation(with:))*