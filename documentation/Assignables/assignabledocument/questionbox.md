# AssignableDocument.QuestionBox

**Framework**: Assignables  
**Kind**: struct

A box on a page for a question.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
struct QuestionBox
```

##### Creating a Question Box

- [`init(id:pageID:bounds:)`](assignabledocument/questionbox/init(id:pageid:bounds:).md)

##### Inspecting the Question Box

- [`bounds`](assignabledocument/questionbox/bounds.md)
- [`AssignableDocument.QuestionBox.ID`](assignabledocument/questionbox/id-swift.typealias.md)
- [`id`](assignabledocument/questionbox/id-swift.property.md)
- [`pageID`](assignabledocument/questionbox/pageid.md)
- [`AssignableDocument.QuestionBox.Document`](assignabledocument/questionbox/document.md)

##### Comparing Question Boxes

- ``==(:)`

##### Hashing the Question Box

- [`hash(into:)`](assignabledocument/questionbox/hash(into:).md)

## Topics

### Operators
- [static func == (AssignableDocument.QuestionBox, AssignableDocument.QuestionBox) -> Bool](assignabledocument/questionbox/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(id: AssignableDocument.QuestionBox.ID, pageID: AssignableDocument.Page.ID, bounds: CGRect)](assignabledocument/questionbox/init(id:pageid:bounds:).md)
  Initialize a question box.
### Instance Properties
- [var bounds: CGRect](assignabledocument/questionbox/bounds.md)
  The bounds of the question box on the page.
- [var hashValue: Int](assignabledocument/questionbox/hashvalue.md)
  The hash value.
- [var id: AssignableDocument.QuestionBox.ID](assignabledocument/questionbox/id-swift.property.md)
  The stable identity of this box.
- [var pageID: AssignableDocument.Page.ID?](assignabledocument/questionbox/pageid.md)
  A read-only property providing the identifier of the page that owns this question box. If the box is not yet assigned to a page, this value is `nil`.
### Instance Methods
- [func hash(into: inout Hasher)](assignabledocument/questionbox/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [AssignableDocument.QuestionBox.Document](assignabledocument/questionbox/document.md)
  The document type this element is for.
- [AssignableDocument.QuestionBox.ID](assignabledocument/questionbox/id-swift.typealias.md)
  A type representing the stable identity of this box.
### Default Implementations
- [Equatable Implementations](assignabledocument/questionbox/equatable-implementations.md)

## Relationships

### Conforms To
- [AssignableDocumentElement](assignabledocumentelement.md)
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
- [AssignableDocument.Question](assignabledocument/question.md)
  A question in the assignable document.
- [var questions: [AssignableDocument.Question]](assignabledocument/questions.md)
  A collection of questions defined for this assignable.
- [AssignableDocument.Element](assignabledocument/element.md)
  The type for elements of this document. An element is a component of the document such as a page or question.
- [var pagesDebugDescription: String](assignabledocument/pagesdebugdescription.md)
- [AssignableDocument.Error](assignabledocument/error.md)
  Errors for this document type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/questionbox)*