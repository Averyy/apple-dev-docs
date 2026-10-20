# questions(on:)

**Framework**: Assignables  
**Kind**: method  
**Role**: Instance Method

Find questions that exist on the specified page.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS

## Declaration

```swift
func questions(on pageID: AssignableDocument.Page.ID) -> [AssignableDocument.Question]
```

#### Return Value

Questions on the specified page.

## Parameters

- `pageID`: The identifier of the page that contains the questions being sought.

## See Also

### Getting and setting the questions
- [func appendQuestion(pageID: AssignableDocument.Page.ID, rect: CGRect, maxScore: Double?) -> AssignableDocument.Question.ID](./appendquestion%28pageid,rect,maxscore%29.md)
  Creates a new question and appends it to the document.
- [func removeQuestion(AssignableDocument.Question.ID) -> AssignableDocument.Question?](./removequestion%28_%29.md)
  Removes a question and its boxes from the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/questions(on:))*