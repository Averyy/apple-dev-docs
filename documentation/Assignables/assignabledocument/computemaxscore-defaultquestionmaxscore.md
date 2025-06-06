# computeMaxScore(defaultQuestionMaxScore:)

**Framework**: Assignables  
**Kind**: method

Computes the maximum possible score for this `AssignableDocument` as defined by each individual question’s `maxScore`.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
func computeMaxScore(defaultQuestionMaxScore: Double? = Double.zero) -> Double?
```

#### Return Value

The maximum possible score for this `AssignableDocument` as defined by each individual question’s `maxScore`. `nil` is returned, if any individual’s `maxScore` is `nil` and `defaultQuestionMaxScore` is `nil`.

## Parameters

- `defaultQuestionMaxScore`: If a question has a     value, the value that should be used instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/computemaxscore(defaultquestionmaxscore:))*