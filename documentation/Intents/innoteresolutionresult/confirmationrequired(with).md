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

> **Deprecated**: INNoteResolutionResult is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class func confirmationRequired(with noteToConfirm: INNote?) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithNoteToConfirm:(INNote *) noteToConfirm;
```

## Return Value

A new [`INNoteResolutionResult`](../innoteresolutionresult.md) object.

## Discussion

Use this method when you locate a single note but cannot determine with enough certainty that it is the one intended by the user. For example, you might ask for confirmation when the note text does not match precisely. Provide an [`INNote`](../innote.md) object with as much information about the note as you have available.

## Parameters

- `noteToConfirm`: The object that resolves the request but must be confirmed by the user.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INNote) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func disambiguation(with: [INNote]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/innoteresolutionresult/confirmationrequired(with:))*