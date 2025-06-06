# AssignableDocumentConfiguration

**Framework**: Assignables  
**Kind**: protocol

A type that specifies the options for an assignable document.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
protocol AssignableDocumentConfiguration : Hashable
```

## Topics

### Configuring a document
- [var maxScore: Double?](assignabledocumentconfiguration/maxscore.md)
  An optional maximum score for this assessment. If `nil`, this value will be synthesized from the question data and associated annotations.
- [var correctScoreMarkType: AssignableDocument.CorrectMarkType](assignabledocumentconfiguration/correctscoremarktype.md)
  The glyph to use for a correct score mark in the assessment.
- [var pointsPerBonusScoreMark: Double](assignabledocumentconfiguration/pointsperbonusscoremark.md)
  The value of each bonus score mark in the assessment.
- [var pointsPerCorrectScoreMark: Double](assignabledocumentconfiguration/pointspercorrectscoremark.md)
  The value of each correct score mark in the assessment.
- [var pointsPerIncorrectScoreMark: Double](assignabledocumentconfiguration/pointsperincorrectscoremark.md)
  The value of each incorrect score mark in the assessment.

## Relationships

### Inherits From
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [protocol AssignedWorkDocumentConfiguration](assignedworkdocumentconfiguration.md)
  A type that specifies the score of a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentconfiguration)*