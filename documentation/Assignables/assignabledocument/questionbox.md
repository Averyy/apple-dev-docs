# AssignableDocument.QuestionBox

**Framework**: Assignables  
**Kind**: struct  
**Role**: Structure

A box on a page for a question.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS

## Declaration

```swift
struct QuestionBox
```

##### Creating a question box

- [`init(id:pageID:bounds:)`](./questionbox/init%28id,pageid,bounds%29.md)

##### Inspecting the question box

- [`bounds`](./questionbox/bounds.md)
- [`AssignableDocument.QuestionBox.ID`](./questionbox/id-swift.typealias.md)
- [`id`](./questionbox/id-swift.property.md)
- [`pageID`](./questionbox/pageid.md)
- [`AssignableDocument.QuestionBox.Document`](./questionbox/document.md)

##### Comparing question boxes

- ``==(*:*:)`

##### Hashing the question box

- [`hash(into:)`](./questionbox/hash%28into%29.md)

## Topics

### Operators
- [static func == (AssignableDocument.QuestionBox, AssignableDocument.QuestionBox) -> Bool](./questionbox/eqeq%28_,_%29.md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(id: AssignableDocument.QuestionBox.ID, pageID: AssignableDocument.Page.ID, bounds: CGRect)](./questionbox/init%28id,pageid,bounds%29.md)
  Initialize a question box.
### Instance Properties
- [var bounds: CGRect](./questionbox/bounds.md)
  The bounds of the question box on the page.
- [var id: AssignableDocument.QuestionBox.ID](./questionbox/id-swift.property.md)
  The stable identity of this box.
- [var pageID: AssignableDocument.Page.ID?](./questionbox/pageid.md)
  A read-only property providing the identifier of the page that owns this question box. If the box is not yet assigned to a page, this value is `nil`.
### Instance Methods
- [func hash(into: inout Hasher)](./questionbox/hash%28into%29.md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [AssignableDocument.QuestionBox.Document](./questionbox/document.md)
  The document type this element is for.
- [AssignableDocument.QuestionBox.ID](./questionbox/id-swift.typealias.md)
  A type representing the stable identity of this box.

## Relationships

### Conforms To
- [AssignableDocumentElement](../assignabledocumentelement.md)
- [DocumentElement](../documentelement.md)
- [Equatable](../../Swift/equatable.md)
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
- [AssignableDocument.Question](./question.md)
  A question in the assignable document.
- [var questions: [AssignableDocument.Question]](./questions.md)
  A collection of questions defined for this assignable.
- [AssignableDocument.Element](./element.md)
  The type for elements of this document. An element is a component of the document such as a page or question.
- [var pagesDebugDescription: String](./pagesdebugdescription.md)
- [AssignableDocument.Error](./error.md)
  Errors for this document type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/questionbox)*