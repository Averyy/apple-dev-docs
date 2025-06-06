# removeQuestion(_:)

**Framework**: Assignables  
**Kind**: method

Removes a question and its boxes from the document.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
@discardableResult
mutating func removeQuestion(_ questionID: AssignableDocument.Question.ID) -> AssignableDocument.Question?
```

## Parameters

- `questionID`: The element to remove.

## See Also

- [func appendQuestion(pageID: AssignableDocument.Page.ID, rect: CGRect, maxScore: Double?) -> AssignableDocument.Question.ID](assignabledocument/appendquestion(pageid:rect:maxscore:).md)
  Creates a new question and appends it to the document.
- [func questions(on: AssignableDocument.Page.ID) -> [AssignableDocument.Question]](assignabledocument/questions(on:).md)
  Find questions that exist on the specified page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/removequestion(_:))*