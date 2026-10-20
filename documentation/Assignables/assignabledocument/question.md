# AssignableDocument.Question

**Framework**: Assignables  
**Kind**: struct  
**Role**: Structure

A question in the assignable document.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS

## Declaration

```swift
struct Question
```

## Topics

### Creating a question
- [init(pageID: AssignableDocument.Page.ID, boxes: [AssignableDocument.QuestionBox], maxScore: Double?)](./question/init%28pageid,boxes,maxscore%29.md)
  Initializes an instance of this object with the given values.
### Inspecting a question
- [var boxes: [AssignableDocument.QuestionBox]](./question/boxes.md)
  The question boxes on pages that denote question regions. Treated as as set.
- [AssignableDocument.Question.ID](./question/id-swift.typealias.md)
  A type representing the stable identity of this question.
- [var id: AssignableDocument.Question.ID](./question/id-swift.property.md)
  The stable identity of this question.
- [var maxScore: Double?](./question/maxscore.md)
  An optional manual maximum point value for this question.
- [AssignableDocument.Question.Thumbnail](./question/thumbnail.md)
  The thumbnail type for this question.
- [AssignableDocument.Question.Document](./question/document.md)
  The document type this element is for.
### Comparing questions
- [static func == (AssignableDocument.Question, AssignableDocument.Question) -> Bool](./question/eqeq%28_,_%29.md)
  Returns a Boolean value indicating whether two values are equal.
### Hashing a question
- [func hash(into: inout Hasher)](./question/hash%28into%29.md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Initializers
- [init(boxes: [AssignableDocument.QuestionBox], maxScore: Double?)](./question/init%28boxes,maxscore%29.md)
  Initializes an instance of this object with the given values.

## Relationships

### Conforms To
- [AssignableDocumentElement](../assignabledocumentelement.md)
- [Copyable](../../Swift/copyable.md)
- [DocumentElement](../documentelement.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Identifiable](../../Swift/identifiable.md)

## See Also

### Inspecting an assignable document
- [AssignableDocument.ID](./id-swift.typealias.md)
  A type representing the stable identity of this document.
- [var id: AssignableDocument.ID](./id-swift.property.md)
  The stable identity of this document.
- [var isMultiPageDocument: Bool](./ismultipagedocument.md)
  `true`, if this document has more than one page; `false`, otherwise.
- [var isPartial: Bool](./ispartial.md)
  Denotes whether or not this document is a partial one.
- [AssignableDocument.PartIDs](./partids-swift.enum.md)
  An enumeration containing the identities of parts managed by this view.
- [var partIDs: [AssignableDocument.PartID]](./partids-swift.property.md)
  Returns a collection of identifiers reflecting the manifest of parts available in the document.
- [AssignableDocument.QuestionBox](./questionbox.md)
  A box on a page for a question.
- [var questions: [AssignableDocument.Question]](./questions.md)
  A collection of questions defined for this assignable.
- [AssignableDocument.Element](./element.md)
  The type for elements of this document. An element is a component of the document such as a page or question.
- [var pagesDebugDescription: String](./pagesdebugdescription.md)
- [AssignableDocument.Error](./error.md)
  Errors for this document type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/question)*