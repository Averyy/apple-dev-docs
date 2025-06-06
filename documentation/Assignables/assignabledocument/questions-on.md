# questions(on:)

**Framework**: Assignables  
**Kind**: method

Find questions that exist on the specified page.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
func questions(on pageID: AssignableDocument.Page.ID) -> [AssignableDocument.Question]
```

#### Return Value

Questions on the specified page.

## Parameters

- `pageID`: The identifier of the page that   contains the questions being sought.

## See Also

- [func appendQuestion(pageID: AssignableDocument.Page.ID, rect: CGRect, maxScore: Double?) -> AssignableDocument.Question.ID](assignabledocument/appendquestion(pageid:rect:maxscore:).md)
  Creates a new question and appends it to the document.
- [func removeQuestion(AssignableDocument.Question.ID) -> AssignableDocument.Question?](assignabledocument/removequestion(_:).md)
  Removes a question and its boxes from the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/questions(on:))*