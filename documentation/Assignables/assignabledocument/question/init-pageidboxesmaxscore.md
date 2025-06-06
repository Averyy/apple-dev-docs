# init(pageID:boxes:maxScore:)

**Framework**: Assignables  
**Kind**: init

Initializes an instance of this object with the given values.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
init(pageID: AssignableDocument.Page.ID, boxes: [AssignableDocument.QuestionBox], maxScore: Double? = nil)
```

## Parameters

- `pageID`: The page ID this question is for.
- `boxes`: The question boxes associated with this   question. Treated as a set.
- `maxScore`: An optional maximum score value   for this question.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/question/init(pageid:boxes:maxscore:))*