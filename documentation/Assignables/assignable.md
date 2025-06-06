# Assignable

**Framework**: Assignables  
**Kind**: protocol

Documents conforming to this protocol can be assigned to a user.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
protocol Assignable
```

## Topics

### Assigning a document
- [func assign(to: AnyUserIdentity) throws -> AssignedWorkDocument](assignable/assign(to:)-4jnsl.md)
  Assign this document to a user.
- [func assign(to: some UserIdentity) throws -> AssignedWorkDocument](assignable/assign(to:)-4mit8.md)
  Assign this document to a user.
### Instance Methods
- [func makeAssignedWorkDocument() throws -> AssignedWorkDocument](assignable/makeassignedworkdocument.md)
  Create a new instance of an [`AssignedWorkDocument`](assignedworkdocument.md).
- [func makeAssignedWorkDocument(id: String) throws -> AssignedWorkDocument](assignable/makeassignedworkdocument(id:).md)
  Create a new instance of an [`AssignedWorkDocument`](assignedworkdocument.md).

## Relationships

### Conforming Types
- [AssignableDocument](assignabledocument.md)

## See Also

- [struct AssignableDocument](assignabledocument.md)
  An assignable document is an augmented PDF that allows teachers to mark up the PDF with the intention of students taking the assessment.
- [struct AssignedWorkDocument](assignedworkdocument.md)
  An assigned work document is a document that contains taker and scorer markup specific to a taker. It also contains a copy of the assignable document upon which it is based.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignable)*