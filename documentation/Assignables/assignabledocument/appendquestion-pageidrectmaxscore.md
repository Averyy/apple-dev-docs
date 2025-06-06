# appendQuestion(pageID:rect:maxScore:)

**Framework**: Assignables  
**Kind**: method

Creates a new question and appends it to the document.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
@discardableResult
mutating func appendQuestion(pageID: AssignableDocument.Page.ID, rect: CGRect, maxScore: Double? = nil) -> AssignableDocument.Question.ID
```

#### Return Value

The newly created question’s ID.

## Parameters

- `pageID`: The ID of the page to append the question to.
- `rect`: The region of the question on the page.

## See Also

- [func questions(on: AssignableDocument.Page.ID) -> [AssignableDocument.Question]](assignabledocument/questions(on:).md)
  Find questions that exist on the specified page.
- [func removeQuestion(AssignableDocument.Question.ID) -> AssignableDocument.Question?](assignabledocument/removequestion(_:).md)
  Removes a question and its boxes from the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/appendquestion(pageid:rect:maxscore:))*