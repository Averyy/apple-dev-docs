---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ocknote"
framework: "CareKit/CareKitStore"
---

# OCKNote

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

`OCKNote` can be attached to all other CareKit objects and values. Use cases may include a physician leaving a note on a task when it is modified to explain why a medication dose was changed, or a note left from a patient to a care provider explaining why they weren’t able to complete a task on a certain occasion.

## Declaration

```swift
struct OCKNote
```

## Topics

### Initializers
- [init(author: String?, title: String?, content: String?)](./ocknote/init%28author,title,content%29.md)
  Initialize a new note with an optional author, title, and content.
- [init(from: any Decoder) throws](./ocknote/init%28from%29.md)
### Instance Properties
- [var author: String?](./ocknote/author.md)
  The person who created this note.
- [var content: String?](./ocknote/content.md)
  The note content.
- [var title: String?](./ocknote/title.md)
  A title for the note.
### Default Implementations
- [Equatable Implementations](./ocknote/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ocknote)*