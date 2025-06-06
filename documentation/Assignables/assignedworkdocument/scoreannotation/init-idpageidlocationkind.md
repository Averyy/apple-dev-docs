# init(id:pageID:location:kind:)

**Framework**: Assignables  
**Kind**: init

Initializes an instance of this object with the given values.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
init(id: AssignedWorkDocument.ScoreAnnotation.ID, pageID: AssignedWorkDocument.Page.ID?, location: CGPoint, kind: AssignedWorkDocument.ScoreAnnotation.Kind)
```

## Parameters

- `id`: The ID of this score annotation.
- `pageID`: The ID of the page that this score annotation is on.
- `location`: The location of the score annotation on the associated page.
- `kind`: The kind of score annotation this is. e.g. Incorrect or correct mark.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocument/scoreannotation/init(id:pageid:location:kind:))*