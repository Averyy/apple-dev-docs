# subscript(_:)

**Framework**: Assignables  
**Kind**: subscript  
**Role**: Instance Subscript

Access the question that the identifier denotes, if any.

**Availability**:
- iOS 17.4+ - Deprecated in 26.0
- iPadOS 17.4+ - Deprecated in 26.0
- Mac Catalyst 17.4+ - Deprecated in 26.0
- visionOS

> **Deprecated**: Access questions using AssignableDocument's questions array instead

## Declaration

```swift
subscript(questionID: AssignableDocument.Question.ID) -> AssignableDocument.Question? { get set }
```

## See Also

### Accessing documents
- [subscript(AssignableDocument.Page.ID) -> AssignableDocument.Page?](./subscript%28_%29-8ou91.md)
  Access the page that the identifier denotes, if any.
- [subscript(AssignableDocument.QuestionBox.ID) -> AssignableDocument.QuestionBox?](./subscript%28_%29-68enn.md)
  Access the question box that the identifier denotes, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/subscript(_:)-7fijz)*