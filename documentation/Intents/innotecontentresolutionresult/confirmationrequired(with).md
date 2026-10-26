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

> **Deprecated**: INNoteContentResolutionResult is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class func confirmationRequired(with noteContentToConfirm: INNoteContent?) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithNoteContentToConfirm:(INNoteContent *) noteContentToConfirm;
```

#### Return Value

A new [`INNoteContentResolutionResult`](../innotecontentresolutionresult.md) object.

#### Discussion

Use this method when you cannot resolve the parameter exactly as intended, but can resolve it to an appropriate value and want the user to confirm that value before continuing.

## Parameters

- `noteContentToConfirm`: The object that resolves the request but must be confirmed by the user.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INNoteContent) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func disambiguation(with: [INNoteContent]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/innotecontentresolutionresult/confirmationrequired(with:))*