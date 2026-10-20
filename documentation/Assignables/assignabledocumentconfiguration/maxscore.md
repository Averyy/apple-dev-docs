# maxScore

**Framework**: Assignables  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An optional maximum score for this assessment. If `nil`, this value will be synthesized from the question data and associated annotations.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS

## Declaration

```swift
var maxScore: Double? { get set }
```

## See Also

### Configuring a document
- [var correctScoreMarkType: AssignableDocument.CorrectMarkType](./correctscoremarktype.md)
  The glyph to use for a correct score mark in the assessment.
- [var pointsPerBonusScoreMark: Double](./pointsperbonusscoremark.md)
  The value of each bonus score mark in the assessment.
- [var pointsPerCorrectScoreMark: Double](./pointspercorrectscoremark.md)
  The value of each correct score mark in the assessment.
- [var pointsPerIncorrectScoreMark: Double](./pointsperincorrectscoremark.md)
  The value of each incorrect score mark in the assessment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentconfiguration/maxscore)*