# AssignedWorkDocument.ScoreAnnotation.Kind

**Framework**: Assignables  
**Kind**: enum  
**Role**: Enumeration

The kind of a score annotation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS

## Declaration

```swift
enum Kind
```

## Topics

### Score annotations
- [AssignedWorkDocument.ScoreAnnotation.Kind.bonus](./kind-swift.enum/bonus.md)
  A score mark indicating a bonus to an answer.
- [AssignedWorkDocument.ScoreAnnotation.Kind.correct](./kind-swift.enum/correct.md)
  A score mark indicating an correct answer.
- [AssignedWorkDocument.ScoreAnnotation.Kind.incorrect](./kind-swift.enum/incorrect.md)
  A score mark indicating an incorrect answer.
- [AssignedWorkDocument.ScoreAnnotation.Kind.unknown](./kind-swift.enum/unknown.md)
  An unknown kind. This value may occur if an older version of this framework is deserializing a newer document version.
### Instance Properties
- [var debugDescription: String](./kind-swift.enum/debugdescription.md)
  A textual representation of this instance, suitable for debugging.

## Relationships

### Conforms To
- [CaseIterable](../../../Swift/caseiterable.md)
- [Copyable](../../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../../Swift/customdebugstringconvertible.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)

## See Also

### Inspecting a score annotation
- [AssignedWorkDocument.ScoreAnnotation.ID](./id-swift.typealias.md)
  A type representing the stable identity of this score annotation.
- [var id: AssignedWorkDocument.ScoreAnnotation.ID](./id-swift.property.md)
  The stable identity of this score annotation.
- [var kind: AssignedWorkDocument.ScoreAnnotation.Kind](./kind-swift.property.md)
  The kind of score annotation this is. e.g. Incorrect or correct mark.
- [var location: CGPoint](./location.md)
  The location of the score annotation on the associated page.
- [var pageID: AssignedWorkDocument.Page.ID?](./pageid.md)
  The ID of the page this score annotation is for.
- [AssignedWorkDocument.ScoreAnnotation.Document](./document.md)
  The document type this element is for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocument/scoreannotation/kind-swift.enum)*