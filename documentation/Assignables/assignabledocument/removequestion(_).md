# removeQuestion(_:)

**Framework**: Assignables  
**Kind**: method  
**Role**: Instance Method

Removes a question and its boxes from the document.

**Availability**:
- iOS 17.4+ - Deprecated in 26.0
- iPadOS 17.4+ - Deprecated in 26.0
- Mac Catalyst 17.4+ - Deprecated in 26.0
- visionOS

> **Deprecated**: Remove questions from AssignableDocument's questions array instead

## Declaration

```swift
@discardableResult
mutating func removeQuestion(_ questionID: AssignableDocument.Question.ID) -> AssignableDocument.Question?
```

## Parameters

- `questionID`: The element to remove.

## See Also

### Getting and setting the questions
- [func appendQuestion(pageID: AssignableDocument.Page.ID, rect: CGRect, maxScore: Double?) -> AssignableDocument.Question.ID](./appendquestion%28pageid,rect,maxscore%29.md)
  Creates a new question and appends it to the document.
- [func questions(on: AssignableDocument.Page.ID) -> [AssignableDocument.Question]](./questions%28on%29.md)
  Find questions that exist on the specified page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/removequestion(_:))*