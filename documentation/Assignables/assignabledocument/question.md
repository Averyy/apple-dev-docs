# AssignableDocument.Question

**Framework**: Assignables  
**Kind**: struct

A question in the assignable document.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
struct Question
```

## Topics

### Creating a question
- [init(pageID: AssignableDocument.Page.ID, boxes: [AssignableDocument.QuestionBox], maxScore: Double?)](assignabledocument/question/init(pageid:boxes:maxscore:).md)
  Initializes an instance of this object with the given values.
### Inspecting a question
- [var boxes: [AssignableDocument.QuestionBox]](assignabledocument/question/boxes.md)
  The question boxes on pages that denote question regions. Treated as as set.
- [AssignableDocument.Question.ID](assignabledocument/question/id-swift.typealias.md)
  A type representing the stable identity of this question.
- [var id: AssignableDocument.Question.ID](assignabledocument/question/id-swift.property.md)
  The stable identity of this question.
- [var maxScore: Double?](assignabledocument/question/maxscore.md)
  An optional manual maximum point value for this question.
- [AssignableDocument.Question.Thumbnail](assignabledocument/question/thumbnail.md)
  The thumbnail type for this question.
- [AssignableDocument.Question.Document](assignabledocument/question/document.md)
  The document type this element is for.
### Comparing questions
- [static func == (AssignableDocument.Question, AssignableDocument.Question) -> Bool](assignabledocument/question/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Hashing a question
- [func hash(into: inout Hasher)](assignabledocument/question/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Initializers
- [init(boxes: [AssignableDocument.QuestionBox], maxScore: Double?)](assignabledocument/question/init(boxes:maxscore:).md)
  Initializes an instance of this object with the given values.
### Instance Properties
- [var hashValue: Int](assignabledocument/question/hashvalue.md)
  The hash value.
### Default Implementations
- [Equatable Implementations](assignabledocument/question/equatable-implementations.md)

## Relationships

### Conforms To
- [AssignableDocumentElement](assignabledocumentelement.md)
- [Copyable](../Swift/Copyable.md)
- [DocumentElement](documentelement.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [AssignableDocument.ID](assignabledocument/id-swift.typealias.md)
  A type representing the stable identity of this document.
- [var id: AssignableDocument.ID](assignabledocument/id-swift.property.md)
  The stable identity of this document.
- [var isMultiPageDocument: Bool](assignabledocument/ismultipagedocument.md)
  `true`, if this document has more than one page; `false`, otherwise.
- [var isPartial: Bool](assignabledocument/ispartial.md)
  Denotes whether or not this document is a partial one.
- [AssignableDocument.PartIDs](assignabledocument/partids-swift.enum.md)
  An enumeration containing the identities of parts managed by this view.
- [var partIDs: [AssignableDocument.PartID]](assignabledocument/partids-swift.property.md)
  Returns a collection of identifiers reflecting the manifest of parts available in the document.
- [AssignableDocument.QuestionBox](assignabledocument/questionbox.md)
  A box on a page for a question.
- [var questions: [AssignableDocument.Question]](assignabledocument/questions.md)
  A collection of questions defined for this assignable.
- [AssignableDocument.Element](assignabledocument/element.md)
  The type for elements of this document. An element is a component of the document such as a page or question.
- [var pagesDebugDescription: String](assignabledocument/pagesdebugdescription.md)
- [AssignableDocument.Error](assignabledocument/error.md)
  Errors for this document type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/question)*