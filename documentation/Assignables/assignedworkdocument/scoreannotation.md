# AssignedWorkDocument.ScoreAnnotation

**Framework**: Assignables  
**Kind**: struct

A score mark on page of the work document.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
struct ScoreAnnotation
```

## Topics

### Creating a score annotation
- [init(id: AssignedWorkDocument.ScoreAnnotation.ID, pageID: AssignedWorkDocument.Page.ID?, location: CGPoint, kind: AssignedWorkDocument.ScoreAnnotation.Kind)](assignedworkdocument/scoreannotation/init(id:pageid:location:kind:).md)
  Initializes an instance of this object with the given values.
### Inspecting a score annotation
- [AssignedWorkDocument.ScoreAnnotation.ID](assignedworkdocument/scoreannotation/id-swift.typealias.md)
  A type representing the stable identity of this score annotation.
- [var id: AssignedWorkDocument.ScoreAnnotation.ID](assignedworkdocument/scoreannotation/id-swift.property.md)
  The stable identity of this score annotation.
- [AssignedWorkDocument.ScoreAnnotation.Kind](assignedworkdocument/scoreannotation/kind-swift.enum.md)
  The kind of a score annotation.
- [var kind: AssignedWorkDocument.ScoreAnnotation.Kind](assignedworkdocument/scoreannotation/kind-swift.property.md)
  The kind of score annotation this is. e.g. Incorrect or correct mark.
- [var location: CGPoint](assignedworkdocument/scoreannotation/location.md)
  The location of the score annotation on the associated page.
- [var pageID: AssignedWorkDocument.Page.ID?](assignedworkdocument/scoreannotation/pageid.md)
  The ID of the page this score annotation is for.
- [AssignedWorkDocument.ScoreAnnotation.Document](assignedworkdocument/scoreannotation/document.md)
  The document type this element is for.
### Comparing score annotations
- [static func == (AssignedWorkDocument.ScoreAnnotation, AssignedWorkDocument.ScoreAnnotation) -> Bool](assignedworkdocument/scoreannotation/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Hashing the score annotation
- [func hash(into: inout Hasher)](assignedworkdocument/scoreannotation/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Instance Properties
- [var hashValue: Int](assignedworkdocument/scoreannotation/hashvalue.md)
  The hash value.
### Default Implementations
- [Equatable Implementations](assignedworkdocument/scoreannotation/equatable-implementations.md)

## Relationships

### Conforms To
- [AssignedWorkDocumentElement](assignedworkdocumentelement.md)
- [Copyable](../Swift/Copyable.md)
- [DocumentElement](documentelement.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [func computeScore() -> Double](assignedworkdocument/computescore.md)
  Gathers all of the points based on all the `AssignedWorkDocument.ScoreAnnotation`s in the document and its `kind` property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocument/scoreannotation)*