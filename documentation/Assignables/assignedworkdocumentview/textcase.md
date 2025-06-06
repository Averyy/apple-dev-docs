# textCase(_:)

**Framework**: Assignables  
**Kind**: method

Sets a transform for the case of the text contained in this view when displayed.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func textCase(_ textCase: Text.Case?) -> some View
```

#### Return Value

A view that transforms the case of the text.

#### Discussion

The default value is `nil`, displaying the text without any case changes.

## Parameters

- `textCase`: One of the   enumerations; the   default is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocumentview/textcase(_:))*