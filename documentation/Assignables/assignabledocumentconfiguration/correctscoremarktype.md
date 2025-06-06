# correctScoreMarkType

**Framework**: Assignables  
**Kind**: property  
**Required**: Yes

The glyph to use for a correct score mark in the assessment.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
var correctScoreMarkType: AssignableDocument.CorrectMarkType { get set }
```

## See Also

- [var maxScore: Double?](assignabledocumentconfiguration/maxscore.md)
  An optional maximum score for this assessment. If `nil`, this value will be synthesized from the question data and associated annotations.
- [var pointsPerBonusScoreMark: Double](assignabledocumentconfiguration/pointsperbonusscoremark.md)
  The value of each bonus score mark in the assessment.
- [var pointsPerCorrectScoreMark: Double](assignabledocumentconfiguration/pointspercorrectscoremark.md)
  The value of each correct score mark in the assessment.
- [var pointsPerIncorrectScoreMark: Double](assignabledocumentconfiguration/pointsperincorrectscoremark.md)
  The value of each incorrect score mark in the assessment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentconfiguration/correctscoremarktype)*