# INNoteContentTypeResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for the type of data contained in notes.

**Availability**:
- iOS 11.0+ - Deprecated in 13.0
- iPadOS 11.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 6.0

> **Deprecated**: This resolution result is no longer used

## Declaration

```swift
class INNoteContentTypeResolutionResult
```

```objc
@interface INNoteContentTypeResolutionResult : INIntentResolutionResult
```

## Overview

You return an [`INNoteContentTypeResolutionResult`](./innotecontenttyperesolutionresult.md) object when resolving parameters containing an [`INNoteContentType`](./innotecontenttype.md) value. Use the creation method that best reflects your ability to resolve the parameter successfully.

For additional resolution operators, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func success(with: INNoteContentType) -> Self](./innotecontenttyperesolutionresult/success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: INNoteContentType) -> Self](./innotecontenttyperesolutionresult/confirmationrequired%28with%29.md)
  Creates an object whose resolution requires confirmation from the user before proceeding.

## Relationships

### Inherits From
- [INIntentResolutionResult](./inintentresolutionresult.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Note Content
- [enum INNoteContentType](./innotecontenttype.md)
  Constants indicating the type of content represented by the note.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/innotecontenttyperesolutionresult)*