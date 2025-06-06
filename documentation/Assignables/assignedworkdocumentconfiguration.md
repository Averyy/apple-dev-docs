# AssignedWorkDocumentConfiguration

**Framework**: Assignables  
**Kind**: protocol

A type that specifies the score of a document.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
protocol AssignedWorkDocumentConfiguration : Hashable
```

## Topics

### Configuring the score
- [var manualScore: Double?](assignedworkdocumentconfiguration/manualscore.md)
  An optional manual score for this work. If `nil`, the work score can be synthesized from the question data and associated annotations.

## Relationships

### Inherits From
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [protocol AssignableDocumentConfiguration](assignabledocumentconfiguration.md)
  A type that specifies the options for an assignable document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocumentconfiguration)*