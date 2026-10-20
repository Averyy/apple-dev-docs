# subscript(_:)

**Framework**: Assignables  
**Kind**: subscript  
**Role**: Instance Subscript

Access the question box that the identifier denotes, if any.

**Availability**:
- iOS 17.4+ - Deprecated in 26.0
- iPadOS 17.4+ - Deprecated in 26.0
- Mac Catalyst 17.4+ - Deprecated in 26.0
- visionOS

> **Deprecated**: Access question boxes using AssignableDocument's question's boxes array instead

## Declaration

```swift
subscript(questionBoxID: AssignableDocument.QuestionBox.ID) -> AssignableDocument.QuestionBox? { get set }
```

## See Also

### Accessing documents
- [subscript(AssignableDocument.Page.ID) -> AssignableDocument.Page?](./subscript%28_%29-8ou91.md)
  Access the page that the identifier denotes, if any.
- [subscript(AssignableDocument.Question.ID) -> AssignableDocument.Question?](./subscript%28_%29-7fijz.md)
  Access the question that the identifier denotes, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/subscript(_:)-68enn)*